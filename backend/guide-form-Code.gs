/**
 * Sedona Wine Tours - Guide Tour Form backend
 * Bound to: Sedona Wine Tours Master Database (Google Sheet)
 * Deploy: Extensions - Apps Script - Deploy - New deployment - Web app
 *         Execute as: Me   -   Who has access: Anyone
 *
 * All calculations live here (never in the browser) so the numbers in the sheet are authoritative.
 * Rules are read from the "Rules" tab on every request, so Jim can change a rate there and the next
 * submission uses it. Migrated rows are never touched.
 */

var SS_ID = '1hHq4MiyVhrSApYO3MKpa1z8yQWPk-AGnmlVTm7qAGUY';
var TZ = 'America/Phoenix';

var TAB = {
  rules: 'Rules', guides: 'Guides', vendors: 'Vendors', cd: 'Customer Database', fh: 'FH Bookings', fhraw: 'FH Raw',
  archive: 'Archive', alerts: 'Alerts', subs: 'Submissions', customers: 'Customers'
};

// Customer Database columns (1-based)
var CD = { id:1, date:2, bookingId:3, division:4, tour:5, guide:6, guide2:7, trainee:8, clients:9, adults:10, kids:11, pets:12,
  pickupLoc:13, pickupZone:14, start:15, finish:16, bookedHrs:17, actualHrs:18, otYN:19, otHrs:20, otAmt:21, fhPaid:22, builtIn:23,
  cardGrat:24, fhFee:25, cardFee:26, webFee:27, revenue:28, tip:29, tipMethod:30, tourDetails:31, custDetails:32, expItem:33,
  vendorTotal:34, cashReimb:35, guidePayTotal:36, pickupTotal:37, fiveStar:38, totalExp:39, net:40, fotaflo:41, photos:42,
  emailed:43, submittedBy:44, submittedAt:45, source:46, subId:47 };
// Payroll tab columns
var PR = { date:1, bookingId:2, tour:3, clients:4, hours:5, pay:6, cash:7, pickup:8, tipMethod:9, tipAmt:10, direct:11, directAmt:12,
  blank:13, charged:14, chargedAmt:15, fiveStar:16, totalDue:17, payment:18, owed:19, rate:20, recordId:21, source:22 };

var KID_CHARGE_TOURS = ['scenic sedona', 'ancient indian ruins', 'historic jerome', 'vortex visions', 'vines & vistas', 'vines and vistas'];
var DIVISIONS = ['Wine Tours of Sedona', 'SIP Sedona', 'Sedona Wine Adventures'];
var TIP_METHODS = ['Cash', 'Venmo/Zelle/PayPal', 'Built-in Gratuity', "Bill Customer's Card"];

// ---------------------------------------------------------------- utilities
function ss() { return SpreadsheetApp.openById(SS_ID); }
function sh(name) { var s = ss().getSheetByName(name); if (!s) throw new Error('Missing tab: ' + name); return s; }
function now() { return new Date(); }
function fmtDate(d) { return Utilities.formatDate(d, TZ, 'EEE, MMM d, yyyy'); }
function iso(d) { return Utilities.formatDate(d, TZ, "yyyy-MM-dd'T'HH:mm:ss"); }
function ymd(d) { return Utilities.formatDate(d, TZ, 'yyyy-MM-dd'); }
function round2(n) { return Math.round((Number(n) || 0) * 100) / 100; }
function roundQuarter(h) { return Math.round((Number(h) || 0) * 4) / 4; }
function num(v) { if (v === '' || v === null || v === undefined) return 0; var n = Number(String(v).replace(/[$,]/g, '')); return isNaN(n) ? 0 : n; }
function json(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function uid(prefix) { return prefix + Utilities.formatDate(now(), TZ, 'yyMMddHHmmss') + Math.floor(Math.random() * 900 + 100); }

function tableRows(sheet) {
  var v = sheet.getDataRange().getValues(); var h = v.shift();
  return v.filter(function (r) { return r.join('') !== ''; }).map(function (r) { var o = {}; h.forEach(function (k, i) { o[String(k).trim()] = r[i]; }); return o; });
}

function secret() {
  var p = PropertiesService.getScriptProperties(); var s = p.getProperty('SECRET');
  if (!s) { s = Utilities.getUuid() + Utilities.getUuid(); p.setProperty('SECRET', s); }
  return s;
}
function hmac(str) {
  return Utilities.computeHmacSha256Signature(str, secret()).map(function (b) { return ('0' + (b & 255).toString(16)).slice(-2); }).join('');
}

// ---------------------------------------------------------------- rules & reference data
function rules() {
  var R = { rate: {}, otAdult: {}, otKid: 35, hoursAddOn: 1, zones: [], builtIn: {}, builtInMinParty: {}, cardPct: 0.023, cardFixed: 0.30, webPct: 0.01, fiveStar: 20 };
  tableRows(sh(TAB.rules)).forEach(function (r) {
    var rule = String(r['Rule']).trim(), key = String(r['Key']).trim(), val = num(r['Value']);
    if (rule === 'Guide rate') R.rate[key] = val;
    else if (rule === 'Overtime adult rate') R.otAdult[key] = val;
    else if (rule === 'Overtime kid rate') R.otKid = val;
    else if (rule === 'Paid hours add-on') R.hoursAddOn = val;
    else if (rule === 'Pickup zone hours') R.zones.push({ zone: key, hours: val });
    else if (rule === 'Built-in gratuity') { R.builtIn[key] = val; R.builtInMinParty[key] = /6\+/.test(String(r['Notes'])) ? 6 : 1; }
    else if (rule === 'Card fee') R.cardPct = val;
    else if (rule === 'Card fee fixed') R.cardFixed = val;
    else if (rule === 'Website fee') R.webPct = val;
    else if (rule === '5-star review bonus') R.fiveStar = val;
  });
  return R;
}
function guides() {
  var s = sh(TAB.guides); var rows = tableRows(s);
  return rows.map(function (r) { return { name: String(r['Guide']).trim(), rate: num(r['Hourly Rate']), status: String(r['Status']), role: String(r['Role'] || ''), pin: String(r['PIN'] || '') }; })
    .filter(function (g) { return g.name; });
}
function vendors(includePending) {
  return tableRows(sh(TAB.vendors)).map(function (r) { return { name: String(r['Vendor']).trim(), category: String(r['Category'] || ''), status: String(r['Status'] || 'Active') }; })
    .filter(function (v) { return v.name && (includePending || /active/i.test(v.status)); })
    .sort(function (a, b) { return a.name.toLowerCase() < b.name.toLowerCase() ? -1 : 1; });
}
function kidCharge(tourName) {
  var t = String(tourName || '').toLowerCase();
  return KID_CHARGE_TOURS.some(function (k) { return t.indexOf(k) >= 0; });
}
function divisionFor(booking) {
  var ref = String(booking.ref || booking['Booking Source'] || '').toLowerCase(), item = String(booking.tour || booking['Item / Tour'] || '').toLowerCase();
  if (ref.indexOf('sipsedona') >= 0 || /sip\b|sip &|sip and|sip all day/.test(item)) return 'SIP Sedona';
  if (ref.indexOf('sedonawineadventures') >= 0) return 'Sedona Wine Adventures';
  return 'Wine Tours of Sedona';
}

// ---------------------------------------------------------------- auth
function login(name, pin) {
  var g = guides().filter(function (x) { return x.name.toLowerCase() === String(name).trim().toLowerCase() && /active/i.test(x.status); })[0];
  if (!g || !g.pin || String(pin).trim() !== g.pin) return null;
  return { guide: g.name, role: g.role, isAdmin: g.name === 'Jim', token: g.name + '.' + hmac(g.name + '|' + g.pin) };
}
function requireAuth(p) {
  var tok = String(p.token || ''); var name = tok.split('.')[0];
  var g = guides().filter(function (x) { return x.name === name; })[0];
  if (!g || tok !== g.name + '.' + hmac(g.name + '|' + g.pin)) throw new Error('Not signed in. Please enter your name and PIN again.');
  return g;
}
function requireAdmin(p) { var g = requireAuth(p); if (g.name !== 'Jim') throw new Error('Admin only'); return g; }

// ---------------------------------------------------------------- routing
function doGet(e) { return handle(e.parameter || {}); }
function doPost(e) {
  var p = {};
  try { p = JSON.parse(e.postData.contents); } catch (err) { p = e.parameter || {}; }
  return handle(p);
}
function handle(p) {
  try {
    var a = p.action;
    if (a === 'ping') return json({ ok: true, time: iso(now()) });
    if (a === 'guideNames') return json({ ok: true, data: guides().filter(function (x) { return /active/i.test(x.status); }).map(function (x) { return x.name; }) });
    if (a === 'login') { var s = login(p.guide, p.pin); return json(s ? { ok: true, session: s } : { ok: false, error: 'Name or PIN not recognized.' }); }
    if (a === 'bootstrap') { var g = requireAuth(p); return json({ ok: true, data: bootstrap(g) }); }
    if (a === 'bookings') { var g2 = requireAuth(p); return json({ ok: true, data: bookingsForForm(g2, p.days) }); }
    if (a === 'submit') { var g3 = requireAuth(p); return json({ ok: true, data: submit(g3, p.payload) }); }
    if (a === 'mine') { var g4 = requireAuth(p); return json({ ok: true, data: mySubmissions(g4) }); }
    if (a === 'archiveAndResubmit') { var g5 = requireAuth(p); return json({ ok: true, data: archiveAndResubmit(g5, p.submissionId, p.payload) }); }
    if (a === 'vendorRequest') { var g6 = requireAuth(p); return json({ ok: true, data: vendorRequest(g6, p.name) }); }
    // admin (Jim)
    if (a === 'admin') { var adm = requireAdmin(p); return json({ ok: true, data: admin(adm, p) }); }
    // Zap / sync endpoints (protected by shared key)
    if (a === 'fhUpsert') { requireKey(p); return json({ ok: true, data: fhUpsert(p.bookings || [p.booking]) }); }
    if (a === 'normalizeRaw') { requireKey(p); return json({ ok: true, data: normalizeRaw() }); }
    return json({ ok: false, error: 'Unknown action' });
  } catch (err) {
    return json({ ok: false, error: String(err.message || err) });
  }
}
function requireKey(p) {
  var k = PropertiesService.getScriptProperties().getProperty('SYNC_KEY');
  if (!k || p.key !== k) throw new Error('Bad sync key');
}

// ---------------------------------------------------------------- bootstrap
function bootstrap(g) {
  var R = rules();
  return {
    guide: g.name, isAdmin: g.name === 'Jim',
    guides: guides().filter(function (x) { return /active/i.test(x.status); }).map(function (x) { return { name: x.name, role: x.role }; }),
    vendors: vendors(false),
    zones: R.zones,
    divisions: ['Wine Tours of Sedona', 'SIP Sedona', 'Sedona Wine Adventures'],
    tipMethods: ['Cash', 'Venmo/Zelle/PayPal', 'Built-in Gratuity', "Bill Customer's Card"],
    kidChargeTours: KID_CHARGE_TOURS,
    sheetUrl: ss().getUrl()
  };
}

// ---------------------------------------------------------------- FareHarbor bookings
/** Upsert normalized bookings into FH Bookings (keyed by Booking ID). Each b: see normalizeFH(). */
function fhUpsert(list) {
  var s = sh(TAB.fh); var data = s.getDataRange().getValues(); var h = data[0];
  var idx = {}; for (var i = 1; i < data.length; i++) idx[String(data[i][0])] = i + 1;
  var n = 0;
  (list || []).forEach(function (b) {
    if (!b || !b.bookingId) return;
    var row = [b.bookingId, b.status || 'booked', b.date || '', b.start || '', b.duration || '', b.division || divisionFor(b), b.tour || '', b.customer || '', b.email || '', b.phone || '',
      b.adults || 0, b.kids || 0, b.pets || 0, b.pickup || '', num(b.amountPaid), num(b.subtotal), num(b.builtIn), num(b.bookingFee), num(b.taxes), b.ref || '', b.bookedAt || '', iso(now()),
      JSON.stringify({ end: b.end || '', paymentType: b.paymentType || '', crew: b.crew || '', notes: b.notes || '', customerTypes: b.customerTypes || '' })];
    var r = idx[String(b.bookingId)];
    if (r) s.getRange(r, 1, 1, row.length).setValues([row]); else { s.appendRow(row); idx[String(b.bookingId)] = s.getLastRow(); }
    n++;
  });
  return { upserted: n };
}

/**
 * FH Raw tab (written by the Zapier Zap "FareHarbor -> Google Sheets" and by the hourly backstop poll):
 * Received At | Source | Booking PK | Status | Start At | End At | Item | Contact Name | Email | Phone | Customer Count |
 * Subtotal | Amount Paid | Booking Ref | Source Type | Created At | Customer Types | Custom Field Names | Custom Field Totals |
 * Payment Types | Crew | Pickup | Processed
 * Lists are comma-joined (Zapier line-item style). normalizeRaw() turns each unprocessed row into an FH Bookings upsert.
 */
var FHRAW_HDR = ['Received At', 'Source', 'Booking PK', 'Status', 'Start At', 'End At', 'Item', 'Contact Name', 'Email', 'Phone', 'Customer Count', 'Subtotal', 'Amount Paid', 'Booking Ref', 'Source Type', 'Created At', 'Customer Types', 'Custom Field Names', 'Custom Field Totals', 'Payment Types', 'Crew', 'Pickup', 'Processed'];
function ensureRawTab() { var s = ss().getSheetByName(TAB.fhraw); if (!s) { s = ss().insertSheet(TAB.fhraw); s.appendRow(FHRAW_HDR); s.setFrozenRows(1); } return s; }
function splitList(v) { return String(v == null ? '' : v).split(/\s*,\s*/).filter(function (x) { return x !== ''; }); }
function normalizeRawRow(r) {
  var types = splitList(r['Customer Types']); var adults = 0, kids = 0, pets = 0;
  types.forEach(function (tname) { var t = tname.toLowerCase(); if (/pet|dog/.test(t)) pets++; else if (/child|kid|youth|teen|minor/.test(t)) kids++; else if (/adult|guest|person|passenger|senior|rider|participant/.test(t)) adults++; else if (/private|shuttle|vehicle|group|tour/.test(t)) { /* flat-rate placeholder, not a person */ } else adults++; });
  // names and totals are index-aligned comma lists from the Zap; keep empty slots so the indexes line up
  var names = String(r['Custom Field Names'] == null ? '' : r['Custom Field Names']).split(','); var totals = String(r['Custom Field Totals'] == null ? '' : r['Custom Field Totals']).replace(/^t:/, '').split(','); var builtIn = 0;
  if (names.length === totals.length) names.forEach(function (nme, i) { if (/gratuit|tip/i.test(nme)) builtIn += centsToDollars(totals[i]); });
  else { var gi = -1; names.forEach(function (nme, i) { if (gi < 0 && /gratuit|tip/i.test(nme)) gi = i; }); if (gi >= 0) { var nz = totals.filter(function (t) { return num(t) !== 0; }); if (nz.length === 1) builtIn = centsToDollars(nz[0]); } }
  // custom field totals come in cents from the API; Zapier shows cents too. Treat values >= 100 with no decimal as cents.
  var paid = num(r['Amount Paid']), sub = num(r['Subtotal']);
  if (paid > 0 && Math.round(paid) === paid && String(r['Amount Paid']).indexOf('.') < 0 && paid >= 1000) paid = paid / 100;
  if (sub > 0 && Math.round(sub) === sub && String(r['Subtotal']).indexOf('.') < 0 && sub >= 1000) sub = sub / 100;
  var sa = String(r['Start At'] || ''), ea = String(r['End At'] || '');
  var date = sa.slice(0, 10), start = sa.length >= 16 ? sa.slice(11, 16) : '', end = ea.length >= 16 ? ea.slice(11, 16) : '';
  var dur = (sa && ea) ? Math.round(((new Date(ea).getTime() - new Date(sa).getTime()) / 3600000) * 4) / 4 : '';
  var b = { bookingId: String(r['Booking PK']).replace(/\D/g, ''), status: String(r['Status'] || 'booked'), date: date, start: start ? to12(start) : '', end: end, duration: dur, tour: String(r['Item'] || ''),
    customer: String(r['Contact Name'] || ''), email: String(r['Email'] || ''), phone: String(r['Phone'] || ''), adults: adults || num(r['Customer Count']), kids: kids, pets: pets,
    pickup: pickupFromRaw(r['Pickup']), amountPaid: round2(paid), subtotal: round2(sub), builtIn: round2(builtIn), bookingFee: 0, taxes: 0, ref: String(r['Booking Ref'] || ''), bookedAt: String(r['Created At'] || ''),
    paymentType: splitList(r['Payment Types'])[0] || '', crew: String(r['Crew'] || ''), customerTypes: types.join(',') };
  b.division = divisionFor(b);
  return b;
}
function centsToDollars(v) { var n = num(v); return (Math.round(n) === n && String(v).indexOf('.') < 0 && Math.abs(n) >= 100) ? n / 100 : n; }
/** The Zap maps every custom-field display value into Pickup (comma list). Keep the address-like parts, else the first area name. */
function pickupFromRaw(v) {
  var s = String(v == null ? '' : v).replace(/\n+/g, ', ');
  if (s.indexOf(',') < 0) return s.trim();
  var parts = s.split(/\s*,\s*/).map(function (x) { return x.replace(/^[^:]*address[^:]*:\s*/i, '').trim(); }).filter(Boolean);
  var addr = [], area = [];
  var ADDR = /(\b\d{1,6}\s+[A-Za-z0-9.'\- ]+\b(dr|drive|rd|road|ln|lane|st|street|ave|avenue|way|ct|court|cir|circle|blvd|trail|trl|pl|place|loop|pkwy|hwy|highway)\b)|\bAZ\s*\d{5}\b|\b(resort|hotel|inn|lodge|suites|motel|b&b|ranch|villas?)\b/i;
  var AREA = /^(west sedona|uptown sedona|uptown|village of oak creek|voc|oak creek canyon|sedona|cottonwood|cornville|clarkdale|jerome|flagstaff|munds park|prescott|camp verde|rimrock|lake montezuma|phoenix|scottsdale|tempe|mesa|chandler|glendale|peoria)$/i;
  for (var i = 0; i < parts.length; i++) {
    var p = parts[i];
    if (/^(yes|no|true|false|\d+)$/i.test(p) || /allerg|dietary|restriction|celebrat|occasion|how did you|hear about/i.test(p)) continue;
    if (ADDR.test(p)) addr.push(p); else if (AREA.test(p)) area.push(p);
  }
  if (addr.length) return addr.join(', ');
  if (area.length) return area[0];
  return '';
}
function to12(t) { var p = t.split(':'); var h = Number(p[0]); var ap = h >= 12 ? 'PM' : 'AM'; h = h % 12 || 12; return h + ':' + p[1] + ' ' + ap; }
/** Time-driven (every 5 min) and also callable: process unprocessed FH Raw rows into FH Bookings. */
function normalizeRaw() {
  var s = ensureRawTab(); var v = s.getDataRange().getValues(); if (v.length < 2) return { processed: 0 };
  var h = v[0]; var pIdx = h.indexOf('Processed') + 1; var list = []; var rowsDone = [];
  for (var i = 1; i < v.length; i++) { if (v[i][pIdx - 1]) continue; var o = {}; h.forEach(function (k, j) { o[k] = v[i][j]; }); if (!o['Booking PK']) continue; list.push(normalizeRawRow(o)); rowsDone.push(i + 1); }
  if (list.length) fhUpsert(list);
  rowsDone.forEach(function (rn) { s.getRange(rn, pIdx).setValue(iso(now())); });
  return { processed: list.length };
}
function installTriggers() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'normalizeRaw') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('normalizeRaw').timeBased().everyMinutes(5).create();
  return 'trigger installed';
}

/** Bookings for the picker: today and the previous N days (default 2), with "recorded" flags. */
function bookingsForForm(g, days) {
  days = Number(days) || 2;
  var today = ymd(now()); var from = ymd(new Date(now().getTime() - days * 86400000));
  var recorded = {}; var cd = sh(TAB.cd).getDataRange().getValues();
  for (var i = 1; i < cd.length; i++) { var bid = String(cd[i][CD.bookingId - 1]); if (bid) recorded[bid] = { by: cd[i][CD.submittedBy - 1], subId: cd[i][CD.subId - 1], recordId: cd[i][CD.id - 1] }; }
  var rows = tableRows(sh(TAB.fh)).map(function (r) {
    var raw = {}; try { raw = JSON.parse(r['Raw'] || '{}'); } catch (e) { }
    var d = r['Tour Date'] instanceof Date ? ymd(r['Tour Date']) : String(r['Tour Date']).slice(0, 10);
    return { bookingId: String(r['Booking ID']), status: String(r['Status']), date: d, start: String(r['Start Time']), end: raw.end || '', duration: num(r['Duration (hrs)']),
      division: String(r['Division']), tour: String(r['Item / Tour']), customer: String(r['Customer Name']), email: String(r['Email']), phone: String(r['Phone']),
      adults: num(r['Adults']), kids: num(r['Kids']), pets: num(r['Pets']), pickup: String(r['Pickup Location']), amountPaid: num(r['Amount Paid']), subtotal: num(r['Subtotal']),
      builtIn: num(r['Built-in Gratuity']), ref: String(r['Booking Source']), paymentType: raw.paymentType || '', crew: raw.crew || '', recorded: recorded[String(r['Booking ID'])] || null };
  }).filter(function (b) { return b.date >= from && b.date <= today && !/cancel/i.test(b.status); });
  rows.sort(function (a, b) { return (a.date + a.start) < (b.date + b.start) ? 1 : -1; });
  return { from: from, to: today, bookings: rows };
}

// ---------------------------------------------------------------- calculations (the heart)
/**
 * payload = {
 *  division, guide (primary; defaults to session), secondaryGuide, trainee, pickupZone,
 *  scheduledStart 'HH:mm', scheduledEnd 'HH:mm', startTime 'HH:mm', finishTime 'HH:mm', bookedHours, overtimeBillable (bool), fotaflo ('Yes'|'No'),
 *  bookings: [{ bookingId, manual, date 'yyyy-mm-dd', tour, customer, adults, kids, pets, pickupLocation, amountPaid, builtInFromFH, paymentType, ref,
 *              tourDetails, customerDetails, expenses:[{vendor, amount, paidWith:'Company Card'|'Cash'}], tips:[{method, amount}] }]
 * }
 */
function compute(payload, R) {
  var P = payload; var out = { bookings: [], run: {} };
  var division = P.division;
  var otRate = R.otAdult[division] || 0;
  var toMin = function (t) { if (!t) return null; var m = String(t).match(/(\d{1,2}):(\d{2})\s*(AM|PM)?/i); if (!m) return null; var h = Number(m[1]), mi = Number(m[2]); if (m[3]) { if (/pm/i.test(m[3]) && h < 12) h += 12; if (/am/i.test(m[3]) && h === 12) h = 0; } return h * 60 + mi; };
  var fin = toMin(P.finishTime), schedEnd = toMin(P.scheduledEnd), st = toMin(P.startTime);
  var actualHrs = (fin !== null && st !== null) ? roundQuarter((fin - st) / 60) : null;
  var otHrs = 0;
  if (P.overtimeBillable && fin !== null && schedEnd !== null) otHrs = Math.max(0, roundQuarter((fin - schedEnd) / 60));
  var bookedHrs = roundQuarter(num(P.bookedHours));
  var hoursPaid = bookedHrs + otHrs + R.hoursAddOn;
  var zone = (R.zones.filter(function (z) { return z.zone === P.pickupZone; })[0] || { hours: 0 });
  var zoneHrs = (division === 'SIP Sedona') ? 0 : num(zone.hours);
  var primary = P.guide; var guideList = [primary]; if (P.secondaryGuide) guideList.push(P.secondaryGuide);
  var payGuides = guideList.filter(function (g) { return g !== 'Jim'; }); if (P.trainee) payGuides.push(P.trainee);
  var splitN = guideList.length; // tips split among primary + secondary only (never trainee)

  var nBookings = P.bookings.length;
  var runOtAmt = 0, runRevenue = 0, runVendor = 0, runCash = 0, runBuiltIn = 0, runCard = 0, runDirect = 0, runDirectMethods = {};
  P.bookings.forEach(function (b) {
    var adults = num(b.adults), kids = num(b.kids);
    var otAmt = round2(otHrs * (adults * otRate + (kidCharge(b.tour) ? kids * R.otKid : 0)));
    var amountPaid = round2(num(b.amountPaid));
    // Built-in gratuity: FareHarbor's figure always wins. Without one, apply the rule (18% on SIP/SWA; WTOS only for 6+ paying people),
    // backing it out of the amount paid (which includes the gratuity). A guide-typed figure never changes the payout; a mismatch only raises a check alert.
    var builtIn = round2(num(b.builtInFromFH));
    if (!builtIn && amountPaid > 0) {
      var pct = num((R.builtIn || {})[division]), minParty = num((R.builtInMinParty || {})[division]) || 1;
      if (pct > 0 && (adults + kids) >= minParty) builtIn = round2(amountPaid * pct / (1 + pct));
    }
    var guideBuiltIn = round2((b.tips || []).filter(function (t) { return t.method === 'Built-in Gratuity'; }).reduce(function (s, t) { return s + num(t.amount); }, 0));
    if (guideBuiltIn && Math.abs(guideBuiltIn - builtIn) > 0.01) b._builtInOverride = true;
    var cardGrat = 0, direct = 0, directMethods = [];
    (b.tips || []).forEach(function (t) {
      var a = num(t.amount); if (!a) return;
      if (t.method === 'Built-in Gratuity') return; // handled above
      else if (t.method === "Bill Customer's Card") cardGrat = round2(cardGrat + a);
      else if (TIP_METHODS.indexOf(t.method) >= 0) { direct = round2(direct + a); directMethods.push(t.method); }
      else throw new Error('Unknown tip method: ' + t.method);
    });
    var cardFee = (/card/i.test(b.paymentType || 'card') && amountPaid > 0) ? round2(amountPaid * R.cardPct + R.cardFixed) : 0;
    var webFee = (division !== 'Wine Tours of Sedona' && /sipsedona|sedonawineadventures/i.test(b.ref || '')) ? round2(amountPaid * R.webPct) : 0;
    // Jim takes no payroll, so his share of every tip (direct, built-in and card-charged) stays with the company as tour revenue
    var jimShare = guideList.indexOf('Jim') >= 0 ? round2((direct + builtIn + cardGrat) / splitN) : 0;
    var revenue = round2(amountPaid - builtIn - cardGrat - cardFee - webFee + otAmt + jimShare);
    var vendorTotal = 0, cash = 0, items = [];
    (b.expenses || []).forEach(function (x) { var a = num(x.amount); if (!x.vendor || !a) return; vendorTotal = round2(vendorTotal + a); if (/cash/i.test(x.paidWith)) cash = round2(cash + a); items.push(x.vendor + ' $' + a.toFixed(2) + (/cash/i.test(x.paidWith) ? ' (cash)' : '')); });
    out.bookings.push({ b: b, adults: adults, kids: kids, pets: num(b.pets), otAmt: otAmt, builtIn: builtIn, cardGrat: cardGrat, direct: direct, directMethods: directMethods.join('/'),
      amountPaid: amountPaid, cardFee: cardFee, webFee: webFee, revenue: revenue, vendorTotal: vendorTotal, cash: cash, items: items.join(' - ') });
    runOtAmt += otAmt; runRevenue += revenue; runVendor += vendorTotal; runCash += cash; runBuiltIn += builtIn; runCard += cardGrat; runDirect += direct;
    directMethods.forEach(function (m) { runDirectMethods[m] = 1; });
  });

  // payroll per paid guide
  var payroll = payGuides.map(function (name) {
    var rate = num(R.rate[name]); var isTrainee = name === P.trainee;
    var pay = round2(hoursPaid * rate), pickup = round2(zoneHrs * rate);
    var charged = isTrainee ? 0 : round2((runBuiltIn + runCard) / splitN);
    var directShare = isTrainee ? 0 : round2(runDirect / splitN);
    var cashShare = (name === primary) ? round2(runCash) : 0; // reimburse whoever paid: the primary guide reports expenses
    var totalDue = round2(pay + cashShare + pickup + charged);
    return { name: name, rate: rate, hoursPaid: hoursPaid, pay: pay, pickup: pickup, cash: cashShare, charged: charged, chargedKind: runCard > 0 && runBuiltIn > 0 ? 'Built-in Gratuity + Bill Customers Card' : (runCard > 0 ? 'Bill Customers Card' : (runBuiltIn > 0 ? 'Built-in Gratuity' : '')), direct: directShare, directMethods: Object.keys(runDirectMethods).join('/'), totalDue: totalDue, isTrainee: isTrainee };
  });
  var guidePayTotal = payroll.reduce(function (s, p) { return s + p.pay; }, 0), pickupTotal = payroll.reduce(function (s, p) { return s + p.pickup; }, 0);
  out.run = { actualHrs: actualHrs, otHrs: otHrs, bookedHrs: bookedHrs, hoursPaid: hoursPaid, zone: P.pickupZone || '', zoneHrs: zoneHrs, payroll: payroll,
    guidePayTotal: round2(guidePayTotal), pickupTotal: round2(pickupTotal), runRevenue: round2(runRevenue), runOtAmt: round2(runOtAmt), runCard: round2(runCard), nBookings: nBookings };
  // expenses allocated per booking: vendor lines belong to the booking; guide pay/pickup are split evenly across bookings of a run
  out.bookings.forEach(function (x) {
    x.guidePayShare = round2(guidePayTotal / nBookings); x.pickupShare = round2(pickupTotal / nBookings);
    x.totalExp = round2(x.vendorTotal + x.guidePayShare + x.pickupShare);
    x.net = round2(x.revenue - x.totalExp);
  });
  return out;
}

// ---------------------------------------------------------------- submit
function submit(g, P) {
  if (!P || !P.bookings || !P.bookings.length) throw new Error('No bookings in submission');
  if (!P.division) throw new Error('Division is required');
  var divMatch = DIVISIONS.filter(function (d) { return d.toLowerCase() === String(P.division).trim().toLowerCase(); })[0];
  if (!divMatch) throw new Error('Unknown division: ' + P.division); P.division = divMatch;
  P.guide = P.guide || g.name;
  if (P.guide !== g.name && g.name !== 'Jim') throw new Error('You can only submit your own tours');
  var known = {}; guides().forEach(function (x) { if (/active/i.test(x.status)) known[x.name] = true; });
  if (!known[P.guide]) throw new Error('Unknown guide: ' + P.guide);
  P.secondaryGuide = String(P.secondaryGuide || '').trim(); P.trainee = String(P.trainee || '').trim();
  if (P.secondaryGuide && !known[P.secondaryGuide]) throw new Error('Unknown second guide: ' + P.secondaryGuide);
  if (P.trainee && !known[P.trainee]) throw new Error('Unknown trainee: ' + P.trainee);
  if (P.secondaryGuide === P.guide) throw new Error('The second guide must be a different person');
  if (P.trainee && (P.trainee === P.guide || P.trainee === P.secondaryGuide)) throw new Error('The trainee must be a different person from the guides');
  // FareHarbor is the source of truth for money and scheduled times: re-read the booking server-side so nothing financial comes from the form
  var fhIdx = {}; tableRows(sh(TAB.fh)).forEach(function (r) { fhIdx[String(r['Booking ID'])] = r; });
  P.bookings.forEach(function (b, i) {
    var f = b.bookingId ? fhIdx[String(b.bookingId).replace(/\D/g, '')] : null; if (!f) return;
    var raw = {}; try { raw = JSON.parse(f['Raw'] || '{}'); } catch (e) { }
    b.amountPaid = num(f['Amount Paid']); b.builtInFromFH = num(f['Built-in Gratuity']); b.paymentType = raw.paymentType || b.paymentType || 'card'; b.ref = String(f['Booking Source'] || b.ref || '');
    if (!b.tour) b.tour = String(f['Item / Tour'] || ''); if (!b.customer) b.customer = String(f['Customer Name'] || '');
    if (i === 0) { if (num(f['Duration (hrs)']) > 0) P.bookedHours = num(f['Duration (hrs)']); if (raw.end) P.scheduledEnd = raw.end; }
  });
  if (num(P.bookedHours) <= 0 || num(P.bookedHours) > 16) throw new Error('Booked tour length must be between 0 and 16 hours');
  P.bookings.forEach(function (b) { if (!String(b.tourDetails || '').trim() || !String(b.customerDetails || '').trim()) throw new Error('Tour details and customer details are required for every booking'); });
  var R = rules(); var C = compute(P, R);
  var subId = uid('S'); var stamp = iso(now());
  var cdSheet = sh(TAB.cd); var recordIds = [];
  var nextNum = cdSheet.getLastRow(); // T#####
  C.bookings.forEach(function (x) {
    var b = x.b; nextNum++;
    var rid = 'T' + ('00000' + nextNum).slice(-5); recordIds.push(rid);
    var dateObj = b.date ? new Date(b.date + 'T12:00:00') : now();
    var tipMethod = x.directMethods || (x.builtIn ? 'Built-in Gratuity' : (x.cardGrat ? "Bill Customer's Card" : 'None'));
    var row = []; row[CD.id - 1] = rid; row[CD.date - 1] = dateObj; row[CD.bookingId - 1] = String(b.bookingId || ''); row[CD.division - 1] = P.division; row[CD.tour - 1] = b.tour || '';
    row[CD.guide - 1] = P.guide; row[CD.guide2 - 1] = P.secondaryGuide || ''; row[CD.trainee - 1] = P.trainee || ''; row[CD.clients - 1] = b.customer || '';
    row[CD.adults - 1] = x.adults; row[CD.kids - 1] = x.kids; row[CD.pets - 1] = x.pets; row[CD.pickupLoc - 1] = b.pickupLocation || ''; row[CD.pickupZone - 1] = P.pickupZone || '';
    row[CD.start - 1] = P.startTime || ''; row[CD.finish - 1] = P.finishTime || ''; row[CD.bookedHrs - 1] = C.run.bookedHrs; row[CD.actualHrs - 1] = C.run.actualHrs;
    row[CD.otYN - 1] = P.overtimeBillable ? 'Yes' : 'No'; row[CD.otHrs - 1] = C.run.otHrs; row[CD.otAmt - 1] = x.otAmt; row[CD.fhPaid - 1] = x.amountPaid; row[CD.builtIn - 1] = x.builtIn;
    row[CD.cardGrat - 1] = x.cardGrat; row[CD.fhFee - 1] = 0; row[CD.cardFee - 1] = x.cardFee; row[CD.webFee - 1] = x.webFee; row[CD.revenue - 1] = x.revenue; row[CD.tip - 1] = x.direct; row[CD.tipMethod - 1] = tipMethod;
    row[CD.tourDetails - 1] = b.tourDetails || ''; row[CD.custDetails - 1] = b.customerDetails || ''; row[CD.expItem - 1] = x.items; row[CD.vendorTotal - 1] = x.vendorTotal; row[CD.cashReimb - 1] = x.cash;
    row[CD.guidePayTotal - 1] = x.guidePayShare; row[CD.pickupTotal - 1] = x.pickupShare; row[CD.fiveStar - 1] = 0; row[CD.totalExp - 1] = x.totalExp; row[CD.net - 1] = x.net;
    row[CD.fotaflo - 1] = P.fotaflo || ''; row[CD.photos - 1] = ''; row[CD.emailed - 1] = ''; row[CD.submittedBy - 1] = g.name; row[CD.submittedAt - 1] = stamp; row[CD.source - 1] = 'Guide Form'; row[CD.subId - 1] = subId;
    for (var i = 0; i < CD.subId; i++) if (row[i] === undefined) row[i] = '';
    cdSheet.appendRow(row);
    upsertCustomer(b, P, x, dateObj);
  });
  // payroll lines (one per paid guide per run)
  var firstB = C.bookings[0].b; var dateObj0 = firstB.date ? new Date(firstB.date + 'T12:00:00') : now();
  var bookingIds = C.bookings.map(function (x) { return x.b.bookingId; }).filter(String).join(', ');
  var clients = C.bookings.map(function (x) { return x.b.customer; }).filter(String).join(' / ');
  var tourName = C.bookings.map(function (x) { return x.b.tour; }).filter(function (v, i, a) { return v && a.indexOf(v) === i; }).join(' / ');
  C.run.payroll.forEach(function (p) {
    var s = ss().getSheetByName(p.name + ' Hours'); if (!s) { s = ss().insertSheet(p.name + ' Hours'); s.appendRow(payrollHeader()); }
    var prevOwed = lastOwed(s);
    var owed = round2(prevOwed + p.totalDue);
    var row = []; row[PR.date - 1] = dateObj0; row[PR.bookingId - 1] = p.isTrainee ? 'TRAINING ' + bookingIds : bookingIds; row[PR.tour - 1] = tourName; row[PR.clients - 1] = clients;
    row[PR.hours - 1] = p.hoursPaid; row[PR.pay - 1] = p.pay; row[PR.cash - 1] = p.cash; row[PR.pickup - 1] = p.pickup; row[PR.tipMethod - 1] = p.directMethods; row[PR.tipAmt - 1] = p.direct;
    row[PR.direct - 1] = p.directMethods; row[PR.directAmt - 1] = p.direct; row[PR.blank - 1] = ''; row[PR.charged - 1] = p.chargedKind; row[PR.chargedAmt - 1] = p.charged; row[PR.fiveStar - 1] = '';
    row[PR.totalDue - 1] = p.totalDue; row[PR.payment - 1] = ''; row[PR.owed - 1] = owed; row[PR.rate - 1] = p.rate; row[PR.recordId - 1] = recordIds.join(', '); row[PR.source - 1] = 'Guide Form ' + subId;
    for (var i = 0; i < PR.source; i++) if (row[i] === undefined) row[i] = '';
    s.appendRow(row);
  });
  // alerts for Jim
  var alerts = [];
  if (C.run.otHrs > 0) alerts.push(addAlert('overtime', bookingIds, P.guide, clients, C.run.otHrs, C.run.runOtAmt, recordIds.join(', '), 'Billable overtime: charge the customer'));
  C.bookings.forEach(function (x) { if (x.cardGrat > 0) alerts.push(addAlert('card-gratuity', x.b.bookingId, P.guide, x.b.customer, '', x.cardGrat, recordIds.join(', '), "Gratuity to charge to the customer's card on file")); });
  C.bookings.forEach(function (x) { if (x.b._builtInOverride) alerts.push(addAlert('check', x.b.bookingId, P.guide, x.b.customer, '', x.builtIn, recordIds.join(', '), 'Guide entered a built-in gratuity different from FareHarbor; please verify')); });
  // submission log
  sh(TAB.subs).appendRow([subId, stamp, g.name, P.division, bookingIds, recordIds.join(', '), JSON.stringify(P), JSON.stringify(C.run)]);
  return { submissionId: subId, recordIds: recordIds, hoursPaid: C.run.hoursPaid, otHours: C.run.otHrs, zoneHours: C.run.zoneHrs, alerts: alerts.length,
    payroll: C.run.payroll.map(function (p) { return { name: p.name, hoursPaid: p.hoursPaid, pickupHours: zoneHrsFor(P, R), charged: p.charged, cash: p.cash }; }) };
}
function zoneHrsFor(P, R) { var z = R.zones.filter(function (z) { return z.zone === P.pickupZone; })[0]; return (P.division === 'SIP Sedona' || !z) ? 0 : z.hours; }
function payrollHeader() { return ['Tour Date', 'Booking ID', 'Tour', 'Clients Name', 'Hours Paid', 'Guide Pay', 'Cash Expenses Reimbursed', 'Pickup Area Additional Costs', 'Tip Method', 'Tip Amount', 'Direct To Guide', 'Amount', '', 'Charged Tips', 'Amount ', '5 Star Review', 'Total Due', 'Payment Amount', 'Total Owed', 'Rate', 'Record ID', 'Source']; }
function lastOwed(s) {
  var v = s.getRange(2, PR.owed, Math.max(1, s.getLastRow() - 1), 1).getValues();
  for (var i = v.length - 1; i >= 0; i--) { if (v[i][0] !== '' && v[i][0] !== null) return num(v[i][0]); }
  return 0;
}
function addAlert(type, bookingId, guide, customer, hours, amount, recordId, note) {
  var s = ss().getSheetByName(TAB.alerts) || ss().insertSheet(TAB.alerts);
  if (s.getLastRow() === 0) s.appendRow(['Alert ID', 'Created', 'Type', 'Booking ID', 'Guide', 'Customer', 'Hours', 'Amount', 'Status', 'Resolved At', 'Record ID', 'Note']);
  var id = uid('A'); s.appendRow([id, iso(now()), type, String(bookingId), guide, customer, hours, amount, 'open', '', recordId, note]); return id;
}

// ---------------------------------------------------------------- customers (CRM upsert)
function upsertCustomer(b, P, x, dateObj) {
  try {
    var s = sh(TAB.customers); var h = s.getRange(1, 1, 1, s.getLastColumn()).getValues()[0]; var col = {}; h.forEach(function (k, i) { col[String(k).trim()] = i + 1; });
    var email = String(b.email || '').trim().toLowerCase(); var name = String(b.customer || '').trim();
    var finder = null;
    if (email) finder = s.createTextFinder(email).matchEntireCell(true).findNext();
    if (!finder && name) finder = s.getRange(2, col['Name'], s.getLastRow(), 1).createTextFinder(name).matchEntireCell(true).findNext();
    var hist = ymd(dateObj) + ' | ' + (b.tour || '') + ' | ' + P.division + ' | ' + P.guide + (b.bookingId ? ' | booking ' + b.bookingId : '');
    if (finder) {
      var r = finder.getRow();
      var get = function (k) { return s.getRange(r, col[k]).getValue(); }, set = function (k, v) { s.getRange(r, col[k]).setValue(v); };
      if (!get('Email') && email) set('Email', email); if (!get('Phone') && b.phone) set('Phone', b.phone);
      var first = get('First Tour Date'); if (!(first instanceof Date) || dateObj < first) set('First Tour Date', dateObj);
      var last = get('Last Tour Date'); if (!(last instanceof Date) || dateObj > last) set('Last Tour Date', dateObj);
      set('Tours Taken', num(get('Tours Taken')) + 1); set('Total Spend', round2(num(get('Total Spend')) + x.revenue));
      if (x.pets > 0) set('Dog Owner', 'Yes');
      set('Tour History', (hist + '\n' + String(get('Tour History') || '')).slice(0, 4000));
      if (b.customerDetails) set('Guide Notes', (String(b.customerDetails) + ' || ' + String(get('Guide Notes') || '')).slice(0, 3000));
      if (b.bookingId) set('FareHarbor Booking IDs', (String(get('FareHarbor Booking IDs') || '') + (get('FareHarbor Booking IDs') ? ', ' : '') + b.bookingId).slice(0, 500));
    } else {
      var row = []; for (var i = 0; i < h.length; i++) row.push('');
      var id = 'C' + ('00000' + s.getLastRow()).slice(-5);
      row[col['Customer ID'] - 1] = id; row[col['Name'] - 1] = name; row[col['Email'] - 1] = email; row[col['Phone'] - 1] = b.phone || '';
      row[col['First Tour Date'] - 1] = dateObj; row[col['Last Tour Date'] - 1] = dateObj; row[col['Tours Taken'] - 1] = 1; row[col['Total Spend'] - 1] = x.revenue;
      row[col['Dog Owner'] - 1] = x.pets > 0 ? 'Yes' : ''; row[col['Tour History'] - 1] = hist; row[col['Guide Notes'] - 1] = b.customerDetails || ''; row[col['Sources'] - 1] = 'Guide Form';
      row[col['FareHarbor Booking IDs'] - 1] = b.bookingId || ''; row[col['Date Added'] - 1] = now();
      s.appendRow(row);
    }
  } catch (e) { /* CRM upsert must never block a submission */ }
}

// ---------------------------------------------------------------- my submissions / edit
function mySubmissions(g) {
  var rows = tableRows(sh(TAB.subs)).filter(function (r) { return String(r['Guide']) === g.name || g.name === 'Jim'; });
  return rows.slice(-40).reverse().map(function (r) { var P = {}; try { P = JSON.parse(r['Payload']); } catch (e) { } return { submissionId: r['Submission ID'], submittedAt: r['Submitted At'], guide: r['Guide'], division: r['Division'], bookingIds: r['Booking IDs'], recordIds: r['Record IDs'], payload: P, status: r['Status'] || 'active' }; }).filter(function (x) { return x.status !== 'archived'; });
}
function archiveAndResubmit(g, subId, newPayload) {
  if (!subId) throw new Error('Missing submission id');
  var owner = tableRows(sh(TAB.subs)).filter(function (r) { return String(r['Submission ID']) === subId; })[0];
  if (!owner) throw new Error('Submission not found');
  if (String(owner['Guide']) !== g.name && g.name !== 'Jim') throw new Error('You can only edit your own submissions');
  if (String(owner['Status']) === 'archived') throw new Error('This submission was already replaced; reload and edit the newer one');
  var stamp = iso(now()); var arc = sh(TAB.archive); var oldIds = [];
  // customer database rows
  var cdS = sh(TAB.cd); var v = cdS.getDataRange().getValues();
  for (var i = v.length - 1; i >= 1; i--) if (String(v[i][CD.subId - 1]) === subId) { oldIds.push(String(v[i][CD.id - 1])); arc.appendRow([stamp, g.name, v[i][CD.id - 1], TAB.cd, 'Edited by guide', JSON.stringify(v[i])]); cdS.deleteRow(i + 1); }
  // payroll rows
  guides().forEach(function (gd) {
    var s = ss().getSheetByName(gd.name + ' Hours'); if (!s) return; var pv = s.getDataRange().getValues();
    for (var j = pv.length - 1; j >= 1; j--) if (String(pv[j][PR.source - 1]).indexOf(subId) >= 0) { arc.appendRow([stamp, g.name, pv[j][PR.recordId - 1], gd.name + ' Hours', 'Edited by guide', JSON.stringify(pv[j])]); s.deleteRow(j + 1); }
    recalcOwed(s);
  });
  // alerts - superseded
  var al = ss().getSheetByName(TAB.alerts);
  if (al) { var av = al.getDataRange().getValues(); for (var k = 1; k < av.length; k++) { if (av[k][8] !== 'open') continue; var rid = String(av[k][10] || ''); if (oldIds.some(function (id) { return rid.indexOf(id) >= 0; })) al.getRange(k + 1, 9).setValue('superseded'); } }
  // mark submission archived
  var subS = sh(TAB.subs); var sv = subS.getDataRange().getValues();
  for (var m = 1; m < sv.length; m++) if (String(sv[m][0]) === subId) subS.getRange(m + 1, 9).setValue('archived');
  return submit(g, newPayload);
}
/** Recompute the running Total Owed column of a payroll tab from the first row that came from the form (migrated rows untouched). */
function recalcOwed(s) {
  var v = s.getDataRange().getValues(); if (v.length < 2) return;
  var start = -1; for (var i = 1; i < v.length; i++) if (String(v[i][PR.source - 1]).indexOf('Guide Form') === 0 || String(v[i][PR.source - 1]) === '' ) { start = i; break; }
  if (start < 0) return;
  var owed = start > 1 ? num(v[start - 1][PR.owed - 1]) : 0;
  for (var j = start; j < v.length; j++) { if (v[j].join('') === '') continue; owed = round2(owed + num(v[j][PR.totalDue - 1]) - num(v[j][PR.payment - 1])); s.getRange(j + 1, PR.owed).setValue(owed); }
}

// ---------------------------------------------------------------- vendors
function vendorRequest(g, name) {
  name = String(name || '').trim(); if (!name) throw new Error('Vendor name required');
  var exists = vendors(true).some(function (v) { return v.name.toLowerCase() === name.toLowerCase(); });
  if (!exists) sh(TAB.vendors).appendRow([name, '', '', '', '', '', 'Pending', 'Requested by ' + g.name, fmtDate(now())]);
  return { name: name, status: exists ? 'exists' : 'pending' };
}

// ---------------------------------------------------------------- admin (Command Center)
function admin(g, p) {
  var op = p.op;
  if (op === 'alerts') return tableRows(ss().getSheetByName(TAB.alerts) || sh(TAB.cd)).filter(function (a) { return a['Alert ID'] && (p.all || a['Status'] === 'open'); });
  if (op === 'resolveAlert') { var s = sh(TAB.alerts); var v = s.getDataRange().getValues(); for (var i = 1; i < v.length; i++) if (String(v[i][0]) === String(p.alertId)) { s.getRange(i + 1, 9).setValue(p.status || 'charged'); s.getRange(i + 1, 10).setValue(iso(now())); return { ok: true }; } throw new Error('Alert not found'); }
  if (op === 'vendors') return vendors(true);
  if (op === 'addVendor') { var vs = sh(TAB.vendors); vs.appendRow([String(p.name).trim(), p.category || '', p.contact || '', p.phone || '', p.email || '', p.address || '', 'Active', p.notes || '', fmtDate(now())]); sortVendors(); return vendors(true); }
  if (op === 'setVendor') { var vs2 = sh(TAB.vendors); var vv = vs2.getDataRange().getValues(); for (var j = 1; j < vv.length; j++) if (String(vv[j][0]).toLowerCase() === String(p.name).toLowerCase()) { if (p.status) vs2.getRange(j + 1, 7).setValue(p.status); if (p.category !== undefined) vs2.getRange(j + 1, 2).setValue(p.category); if (p.newName) vs2.getRange(j + 1, 1).setValue(p.newName); sortVendors(); return vendors(true); } throw new Error('Vendor not found'); }
  if (op === 'guides') return guides().map(function (x) { return { name: x.name, rate: x.rate, status: x.status, role: x.role, pin: x.pin }; });
  if (op === 'setPin') { var gs = sh(TAB.guides); var gv = gs.getDataRange().getValues(); var pinCol = gv[0].indexOf('PIN') + 1; for (var k = 1; k < gv.length; k++) if (String(gv[k][0]) === String(p.guide)) { gs.getRange(k + 1, pinCol).setValue(String(p.pin)); return { ok: true }; } throw new Error('Guide not found'); }
  if (op === 'tours') return toursForMonth(p.month);
  if (op === 'payroll') return payrollDue();
  if (op === 'recalc') { guides().forEach(function (gd) { var s = ss().getSheetByName(gd.name + ' Hours'); if (s) recalcOwed(s); }); return { ok: true }; }
  if (op === 'submissions') return tableRows(sh(TAB.subs)).slice(-100).reverse().map(function (r) { return { submissionId: r['Submission ID'], submittedAt: r['Submitted At'], guide: r['Guide'], division: r['Division'], bookingIds: r['Booking IDs'], recordIds: r['Record IDs'], status: r['Status'] || 'active' }; });
  if (op === 'importSheet') {
    // copy a whole tab from another spreadsheet (same account) into this one; mode 'replace' (default) or 'append'
    var src = SpreadsheetApp.openById(p.sourceId).getSheetByName(p.sourceTab); if (!src) throw new Error('Source tab not found');
    var vals = src.getDataRange().getValues(); if (!vals.length) throw new Error('Source empty');
    var tgt = ss().getSheetByName(p.targetTab) || ss().insertSheet(p.targetTab);
    var startRow = 1;
    if (p.mode === 'append') { startRow = tgt.getLastRow() + 1; vals = vals.slice(1); }
    else { tgt.clearContents(); }
    for (var i = 0; i < vals.length; i += 2000) { var chunk = vals.slice(i, i + 2000); tgt.getRange(startRow + i, 1, chunk.length, chunk[0].length).setValues(chunk); }
    if (p.mode !== 'append') { tgt.setFrozenRows(1); tgt.getRange(1, 1, 1, vals[0].length).setFontWeight('bold'); }
    return { rows: vals.length, cols: vals[0].length, target: p.targetTab };
  }
  if (op === 'deleteTab') { var dt = ss().getSheetByName(p.tab); if (!dt) throw new Error('Tab not found'); ss().deleteSheet(dt); return { deleted: p.tab }; }
  if (op === 'normalizeRaw') return normalizeRaw();
  if (op === 'installTriggers') return installTriggers();
  if (op === 'crmQueue') return crmQueue(p);
  if (op === 'crmMark') return crmMark(p);
  if (op === 'syncKey') { var pr = PropertiesService.getScriptProperties(); var k2 = pr.getProperty('SYNC_KEY'); if (!k2) { k2 = Utilities.getUuid(); pr.setProperty('SYNC_KEY', k2); } return { key: k2 }; }
  throw new Error('Unknown admin op');
}
function sortVendors() { var s = sh(TAB.vendors); if (s.getLastRow() > 2) s.getRange(2, 1, s.getLastRow() - 1, s.getLastColumn()).sort({ column: 1, ascending: true }); }
// ---------------------------------------------------------------- CRM sync (Drip / HubSpot), driven by the "Customer CRM sync" scheduled task
function crmQueue(p) {
  var s = sh(TAB.customers); var v = s.getDataRange().getValues(); var h = v[0]; var col = {}; h.forEach(function (k, i) { col[String(k).trim()] = i; });
  var limit = Number(p.limit) || 40; var since = p.since ? new Date(p.since) : null; var out = [];
  for (var i = 1; i < v.length && out.length < limit; i++) {
    var r = v[i]; var email = String(r[col['Email']] || '').trim().toLowerCase(); if (!email || email.indexOf('@') < 0) continue;
    var drip = String(r[col['Drip Status']] || ''); var hs = String(r[col['HubSpot ID']] || '');
    if (drip && (hs || !p.hubspot)) continue;
    var src = String(r[col['Sources']] || ''); var added = r[col['Date Added']];
    if (src.indexOf('Guide Form') < 0 && !(since && added instanceof Date && added >= since)) continue;
    var name = String(r[col['Name']] || '').trim(); var first = String(r[col['First Name']] || '').trim(), last = String(r[col['Last Name']] || '').trim();
    if (!first && name) { var parts = name.replace(/\s*&.*$/, '').split(/\s+/); first = parts[0] || ''; last = parts.slice(1).join(' '); }
    var hist = String(r[col['Tour History']] || '').split('\n')[0].split('|').map(function (x) { return x.trim(); });
    var divs = {}; String(r[col['Tour History']] || '').split('\n').forEach(function (line) { var q = line.split('|'); if (q[2]) divs[q[2].trim()] = 1; });
    out.push({ row: i + 1, customerId: r[col['Customer ID']], name: name, first: first, last: last, email: email, phone: String(r[col['Phone']] || ''), city: r[col['City']] || '', state: r[col['State']] || '',
      firstTour: r[col['First Tour Date']] instanceof Date ? ymd(r[col['First Tour Date']]) : '', lastTour: r[col['Last Tour Date']] instanceof Date ? ymd(r[col['Last Tour Date']]) : '',
      toursTaken: num(r[col['Tours Taken']]), totalSpend: num(r[col['Total Spend']]), dogOwner: /yes/i.test(String(r[col['Dog Owner']] || '')), tags: String(r[col['Tags']] || ''),
      lastTourName: hist[1] || '', lastDivision: hist[2] || '', lastGuide: hist[3] || '', divisions: Object.keys(divs), dripStatus: drip, hubspotId: hs });
  }
  return { count: out.length, customers: out };
}
function crmMark(p) {
  var s = sh(TAB.customers); var h = s.getRange(1, 1, 1, s.getLastColumn()).getValues()[0]; var col = {}; h.forEach(function (k, i) { col[String(k).trim()] = i + 1; });
  var row = Number(p.row); if (!row || row < 2) throw new Error('row required');
  if (p.drip !== undefined) s.getRange(row, col['Drip Status']).setValue(String(p.drip));
  if (p.hubspotId !== undefined) s.getRange(row, col['HubSpot ID']).setValue(String(p.hubspotId));
  if (p.first) s.getRange(row, col['First Name']).setValue(String(p.first)); if (p.last) s.getRange(row, col['Last Name']).setValue(String(p.last));
  return { ok: true, row: row };
}
function toursForMonth(month) {
  month = month || Utilities.formatDate(now(), TZ, 'yyyy-MM');
  var v = sh(TAB.cd).getDataRange().getValues(); var out = [];
  for (var i = 1; i < v.length; i++) {
    var d = v[i][CD.date - 1]; if (!(d instanceof Date)) continue; if (Utilities.formatDate(d, TZ, 'yyyy-MM') !== month) continue;
    out.push({ recordId: v[i][CD.id - 1], date: ymd(d), bookingId: String(v[i][CD.bookingId - 1]), division: v[i][CD.division - 1], tour: v[i][CD.tour - 1], guide: v[i][CD.guide - 1], guide2: v[i][CD.guide2 - 1], trainee: v[i][CD.trainee - 1],
      clients: v[i][CD.clients - 1], adults: v[i][CD.adults - 1], kids: v[i][CD.kids - 1], pets: v[i][CD.pets - 1], start: v[i][CD.start - 1], finish: v[i][CD.finish - 1], hours: v[i][CD.actualHrs - 1], otYN: v[i][CD.otYN - 1], otAmt: v[i][CD.otAmt - 1],
      revenue: v[i][CD.revenue - 1], tip: v[i][CD.tip - 1], tipMethod: v[i][CD.tipMethod - 1], tourDetails: v[i][CD.tourDetails - 1], customerDetails: v[i][CD.custDetails - 1], expenses: v[i][CD.expItem - 1], totalExp: v[i][CD.totalExp - 1], net: v[i][CD.net - 1], fotaflo: v[i][CD.fotaflo - 1], submittedBy: v[i][CD.submittedBy - 1], subId: v[i][CD.subId - 1] });
  }
  return { month: month, tours: out.reverse(), sheetUrl: ss().getUrl() + '#gid=' + sh(TAB.cd).getSheetId() };
}
function payrollDue() {
  return guides().filter(function (g) { return g.name !== 'Jim'; }).map(function (g) {
    var s = ss().getSheetByName(g.name + ' Hours'); if (!s) return { guide: g.name, owed: 0, unpaid: [] };
    var v = s.getDataRange().getValues(); var owed = lastOwed(s); var unpaid = []; var lastPay = null;
    for (var i = v.length - 1; i >= 1; i--) { if (num(v[i][PR.payment - 1]) > 0) { lastPay = { date: v[i][PR.date - 1] instanceof Date ? ymd(v[i][PR.date - 1]) : String(v[i][PR.date - 1]), amount: num(v[i][PR.payment - 1]) }; break; } }
    for (var j = v.length - 1; j >= 1; j--) { if (num(v[j][PR.payment - 1]) > 0) break; if (v[j].join('') === '') continue; unpaid.unshift({ date: v[j][PR.date - 1] instanceof Date ? ymd(v[j][PR.date - 1]) : String(v[j][PR.date - 1]), bookingId: String(v[j][PR.bookingId - 1]), tour: v[j][PR.tour - 1], clients: v[j][PR.clients - 1], hours: v[j][PR.hours - 1], pay: v[j][PR.pay - 1], cash: v[j][PR.cash - 1], pickup: v[j][PR.pickup - 1], charged: v[j][PR.chargedAmt - 1], fiveStar: v[j][PR.fiveStar - 1], totalDue: v[j][PR.totalDue - 1] }); }
    return { guide: g.name, rate: g.rate, owed: owed, lastPayment: lastPay, unpaid: unpaid, sheetUrl: ss().getUrl() + '#gid=' + s.getSheetId() };
  });
}

// ---------------------------------------------------------------- one-time setup (run from the editor)
function setup() {
  var S = ss();
  var gs = sh(TAB.guides); var h = gs.getRange(1, 1, 1, gs.getLastColumn()).getValues()[0];
  if (h.indexOf('PIN') < 0) {
    gs.getRange(1, h.length + 1).setValue('PIN');
    var v = gs.getDataRange().getValues();
    for (var i = 1; i < v.length; i++) { var name = String(v[i][0]); var pin = name === 'Jim' ? '4865' : String(Math.floor(1000 + Math.random() * 9000)); gs.getRange(i + 1, h.length + 1).setValue(pin); }
  }
  if (!S.getSheetByName(TAB.alerts)) S.insertSheet(TAB.alerts).appendRow(['Alert ID', 'Created', 'Type', 'Booking ID', 'Guide', 'Customer', 'Hours', 'Amount', 'Status', 'Resolved At', 'Record ID', 'Note']);
  if (!S.getSheetByName(TAB.subs)) S.insertSheet(TAB.subs).appendRow(['Submission ID', 'Submitted At', 'Guide', 'Division', 'Booking IDs', 'Record IDs', 'Payload', 'Run', 'Status']);
  var cd = sh(TAB.cd); if (cd.getRange(1, CD.subId).getValue() !== 'Submission ID') cd.getRange(1, CD.subId).setValue('Submission ID');
  ensureRawTab();
  secret();
  var pr = PropertiesService.getScriptProperties(); if (!pr.getProperty('SYNC_KEY')) pr.setProperty('SYNC_KEY', Utilities.getUuid());
  return 'setup complete';
}

// ---------------------------------------------------------------- self-test of the math (run from the editor; writes nothing)
function selfTest() {
  var R = { rate: { Juan: 25, Ed: 24, Uma: 20, Jim: 0 }, otAdult: { 'Wine Tours of Sedona': 75, 'Sedona Wine Adventures': 50, 'SIP Sedona': 30 }, otKid: 35, hoursAddOn: 1,
    zones: [{ zone: 'Cornville / Clarkdale / Cottonwood', hours: 1 }, { zone: 'Jerome', hours: 1.5 }, { zone: 'Sedona / Uptown / Oak Creek Canyon / Village of Oak Creek', hours: 0 }], cardPct: 0.023, cardFixed: 0.30, webPct: 0.01, fiveStar: 20 };
  var results = [];
  function check(label, got, want) { results.push((Math.abs(got - want) < 0.005 ? 'PASS ' : 'FAIL ') + label + ': got ' + got + ' want ' + want); }
  // 1) WTOS 3-hr tour, 3 adults, 4:27 actual - 1.5 hr OT billable (4:27 - 3:00 = 1:27 - 1.5), Juan, Cornville pickup, $450 paid by card, no gratuity, cash tasting $40
  var C1 = compute({ division: 'Wine Tours of Sedona', guide: 'Juan', pickupZone: 'Cornville / Clarkdale / Cottonwood', scheduledEnd: '16:00', startTime: '13:00', finishTime: '17:27', bookedHours: 3, overtimeBillable: true,
    bookings: [{ bookingId: '1', tour: 'A Multi-Vineyard & Winery Tasting Experience', customer: 'Test', adults: 3, kids: 0, pets: 0, amountPaid: 450, builtInFromFH: 0, paymentType: 'card', ref: '', tourDetails: 'x', customerDetails: 'y', expenses: [{ vendor: 'Oak Creek Vineyards', amount: 40, paidWith: 'Cash' }], tips: [{ method: 'Cash', amount: 60 }] }] }, R);
  check('1 OT hours', C1.run.otHrs, 1.5); check('1 OT amount', C1.bookings[0].otAmt, 337.5); check('1 hours paid', C1.run.hoursPaid, 5.5);
  check('1 Juan pay', C1.run.payroll[0].pay, 137.5); check('1 pickup', C1.run.payroll[0].pickup, 25); check('1 cash reimb', C1.run.payroll[0].cash, 40); check('1 total due', C1.run.payroll[0].totalDue, 202.5);
  check('1 card fee', C1.bookings[0].cardFee, 10.65); check('1 revenue', C1.bookings[0].revenue, 450 - 10.65 + 337.5); check('1 net', C1.bookings[0].net, round2(776.85 - (40 + 137.5 + 25)));
  // 2) SIP run: two bookings, Ed + trainee Uma, built-in gratuity from FH, website booking (1%), no OT, one guest tips $20 cash
  var C2 = compute({ division: 'SIP Sedona', guide: 'Ed', trainee: 'Uma', pickupZone: 'Cornville / Clarkdale / Cottonwood', scheduledEnd: '17:00', startTime: '13:00', finishTime: '17:05', bookedHours: 4, overtimeBillable: false,
    bookings: [{ bookingId: 'a', tour: '4-Hour SIP & Savor Tour', customer: 'A', adults: 2, amountPaid: 169.92, builtInFromFH: 25.92, paymentType: 'card', ref: 'https://sipsedona.com', tourDetails: 'x', customerDetails: 'y', expenses: [{ vendor: 'Alcantara Vineyards', amount: 30, paidWith: 'Company Card' }], tips: [{ method: 'Cash', amount: 20 }] },
      { bookingId: 'b', tour: '4-Hour SIP & Savor Tour', customer: 'B', adults: 4, amountPaid: 339.84, builtInFromFH: 51.84, paymentType: 'card', ref: 'https://sipsedona.com', tourDetails: 'x', customerDetails: 'y', expenses: [], tips: [] }] }, R);
  check('2 OT hours (not billable)', C2.run.otHrs, 0); check('2 hours paid', C2.run.hoursPaid, 5); check('2 pickup hrs (SIP - 0)', C2.run.payroll[0].pickup, 0);
  check('2 Ed pay', C2.run.payroll[0].pay, 120); check('2 Ed charged tips', C2.run.payroll[0].charged, 77.76); check('2 Ed total due', C2.run.payroll[0].totalDue, 197.76);
  check('2 Uma pay', C2.run.payroll[1].pay, 100); check('2 Uma charged (trainee - 0)', C2.run.payroll[1].charged, 0); check('2 Uma total due', C2.run.payroll[1].totalDue, 100);
  check('2 booking a card fee', C2.bookings[0].cardFee, round2(169.92 * 0.023 + 0.30)); check('2 booking a web fee', C2.bookings[0].webFee, 1.70);
  check('2 booking a revenue', C2.bookings[0].revenue, round2(169.92 - 25.92 - 4.21 - 1.70)); check('2 booking a guide pay share', C2.bookings[0].guidePayShare, 110);
  // 3) two guides, bill customer's card gratuity, Jim primary (no payroll), Ed secondary
  var C3 = compute({ division: 'Wine Tours of Sedona', guide: 'Jim', secondaryGuide: 'Ed', pickupZone: 'Jerome', scheduledEnd: '16:00', startTime: '12:00', finishTime: '16:00', bookedHours: 4, overtimeBillable: false,
    bookings: [{ bookingId: 'c', tour: 'The Terroir of the Verde Valley Wine Trail', customer: 'C', adults: 8, amountPaid: 2400, builtInFromFH: 360, paymentType: 'card', ref: '', tourDetails: 'x', customerDetails: 'y', expenses: [], tips: [{ method: "Bill Customer's Card", amount: 100 }, { method: 'Venmo/Zelle/PayPal', amount: 50 }] }] }, R);
  check('3 payroll count (Jim excluded)', C3.run.payroll.length, 1); check('3 Ed pay', C3.run.payroll[0].pay, 120); check('3 Ed pickup (Jerome 1.5h - 24)', C3.run.payroll[0].pickup, 36);
  check('3 Ed charged (460/2)', C3.run.payroll[0].charged, 230); check('3 Ed direct share', C3.run.payroll[0].direct, 25);
  check('3 revenue (Jim half of 360 built-in + 100 card + 50 Venmo = 255 stays as revenue)', C3.bookings[0].revenue, round2(2400 - 360 - 100 - (2400 * 0.023 + 0.3) + 255));
  // 4) kids overtime on a kid-charge tour, SWA
  var C4 = compute({ division: 'Sedona Wine Adventures', guide: 'Uma', scheduledEnd: '15:00', startTime: '12:00', finishTime: '15:38', bookedHours: 3, overtimeBillable: true,
    bookings: [{ bookingId: 'd', tour: 'Vines & Vistas: Kayak and Wine Experience', customer: 'D', adults: 2, kids: 2, pets: 1, amountPaid: 500, builtInFromFH: 0, paymentType: 'in-store', ref: '', tourDetails: 'x', customerDetails: 'y', expenses: [], tips: [] }] }, R);
  check('4 OT hours (38 min - 0.75)', C4.run.otHrs, 0.75); check('4 OT amount (0.75 - (2-50 + 2-35))', C4.bookings[0].otAmt, 127.5); check('4 card fee (not card - 0)', C4.bookings[0].cardFee, 0);
  Logger.log(results.join('\n')); return results;
}
