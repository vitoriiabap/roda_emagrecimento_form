import smtplib
import email.message


def enviar_email(result_file_name, client_name, client_email):
    html_email_body = f"""
<!DOCTYPE html>
<html lang="pt-BR" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <p>Parabéns, {client_name}!</p>

    <p>Este exercício identificou possíveis<strong> atitudes que podem estar atrapalhando e interrompendo a evolução do
        seu
        emagrecimento.</strong></p>

    <p>Ao longo desse processo de transformação física, <strong>é preciso primeiramente conhecer e desenvolver suas
        ações
        comportamentais!</strong> Dessa forma, você não só conseguirá atingir o seu objetivo, mas também defini-lo e
        mantê-lo.</p>

    <p>Vamos para os próximos passos?</p>
    <a href="https://www.skyvector.com" target="_blank">Converse comigo no Whatsapp</a>
    <div style="text-align: center;">
    <p>
        <img src="https://github.com/vitoriiabap/roda_emagrecimento_form/blob/main/resultados/
{result_file_name}?raw=true"
             alt="foto_teste"
             width="500"
        style="vertical-align:middle;margin:50px 0px">
    </p>

</div>
</body>
</html>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Aqui está seu resultado do TISDE'
    msg['From'] = 'mentoriaviviriba@gmail.com'
    msg['To'] = client_email
    password = 'oxhxkbiasqmsfvby'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html_email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending email_sender
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
