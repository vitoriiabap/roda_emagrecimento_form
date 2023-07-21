import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def enviar_email(client_name, client_email, file_name, imagem):
    html_email_body = f"""
<!DOCTYPE html>
<html lang="pt-BR" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>Parabéns, fulano!</p>

    <p>Este exercício identificou possíveis<strong> atitudes que podem estar atrapalhando e interrompendo a evolução do
        seu
        emagrecimento.</strong></p>

    <p>Ao longo desse processo de transformação física, <strong>é preciso primeiramente conhecer e desenvolver suas
        ações
        comportamentais!</strong> Dessa forma, você não só conseguirá atingir o seu objetivo, mas também defini-lo e
        mantê-lo.</p>
    <img src="{imagem}" alt="Google Drive Image" width="500"/>

    <p>Vamos para os próximos passos?</p>
    <a href="https://www.skyvector.com" target="_blank">Converse comigo no Whatsapp</a>
    <div style="text-align: center;">

</div>
</body>
</html>
    """

    # msg = email.message.Message()
    msg = MIMEMultipart()
    msg['Subject'] = 'Aqui está seu resultado do TISDE'
    msg['From'] = 'mentoriaviviriba@gmail.com'
    msg['To'] = client_email
    password = 'oxhxkbiasqmsfvby'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html_email_body)
    #msg.attach(MIMEText(html_email_body, 'html'))
    # attchment = open(imagem, 'rb')
    #
    # att = MIMEBase('application', 'octet-stream')
    # att.set_payload(attchment.read())
    # encoders.encode_base64(att)
    #
    # att.add_header('Content-Disposition', f'attachment; filename=teste.png')
    # attchment.close()
    # msg.attach(att)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending email_sender
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()
