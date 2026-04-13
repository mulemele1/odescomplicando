<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Configurações
    $to = "jacintodacostamulemele@gmail.com";
    $from_email = "no-reply@triana.co.mz"; // Altere para um domínio válido se tiver
    
    // Pegar e sanitizar os dados
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $cc = filter_var($_POST['cc'], FILTER_SANITIZE_EMAIL);
    $subject = htmlspecialchars($_POST['subject']);
    $message = htmlspecialchars($_POST['message']);
    
    // Validar email obrigatório
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "error_invalid_email";
        exit;
    }
    
    // Validar CC se existir
    if (!empty($cc) && !filter_var($cc, FILTER_VALIDATE_EMAIL)) {
        echo "error_invalid_cc";
        exit;
    }
    
    // Montar o corpo do email
    $body = "========================================\n";
    $body .= "MENSAGEM DO PORTFÓLIO - JACINTO COSTA\n";
    $body .= "========================================\n\n";
    $body .= "De: " . $email . "\n";
    if (!empty($cc)) {
        $body .= "CC: " . $cc . "\n";
    }
    $body .= "Assunto: " . $subject . "\n";
    $body .= "----------------------------------------\n";
    $body .= "MENSAGEM:\n";
    $body .= $message . "\n";
    $body .= "----------------------------------------\n";
    $body .= "Data: " . date("d/m/Y H:i:s") . "\n";
    $body .= "IP: " . $_SERVER['REMOTE_ADDR'] . "\n";
    $body .= "========================================\n";
    
    // Headers do email
    $headers = "From: " . $from_email . "\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    if (!empty($cc)) {
        $headers .= "Cc: " . $cc . "\r\n";
    }
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();
    
    // Enviar email
    $mail_sent = mail($to, $subject, $body, $headers);
    
    if ($mail_sent) {
        echo "success";
    } else {
        echo "error";
    }
} else {
    echo "invalid_request";
}
?>