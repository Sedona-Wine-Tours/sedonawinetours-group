<?php
// Contact form handler for sedonawinetours.group (GoDaddy cPanel / PHP mail)
$to      = "info@winetoursofsedona.com";   // <- change if inquiries should go elsewhere
$subject = "Website inquiry — sedonawinetours.group";

if ($_SERVER["REQUEST_METHOD"] !== "POST") { header("Location: /"); exit; }
if (!empty($_POST["website"])) { header("Location: /thank-you"); exit; } // honeypot: bots fill this

$name     = trim(strip_tags($_POST["name"] ?? ""));
$email    = trim(filter_var($_POST["email"] ?? "", FILTER_SANITIZE_EMAIL));
$phone    = trim(strip_tags($_POST["phone"] ?? ""));
$division = trim(strip_tags($_POST["division"] ?? ""));
$message  = trim(strip_tags($_POST["message"] ?? ""));

if ($name === "" || !filter_var($email, FILTER_VALIDATE_EMAIL) || $message === "") {
  header("Location: /#contact"); exit;
}

$body  = "Name: $name\nEmail: $email\nPhone: $phone\nDivision: $division\n\n$message\n\n— Sent from the contact form on www.sedonawinetours.group";
$headers = "From: website@sedonawinetours.group\r\nReply-To: $email\r\nContent-Type: text/plain; charset=UTF-8\r\n";
@mail($to, $subject, $body, $headers);
header("Location: /thank-you"); exit;
