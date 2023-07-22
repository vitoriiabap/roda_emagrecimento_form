import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def enviar_email(client_name, client_email, imagem):
    with open('email_sender/email_body.html', 'r', encoding='utf-8') as arquivo_html:
        html_content = arquivo_html.read().replace('fulano', client_name)

    msg = MIMEMultipart()
    msg['From'] = 'mentoriaviviriba@gmail.com'
    recipients = [client_email, 'mentoriaviviriba@gmail.com']
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'Aqui está seu resultado do TISDE'
    password = 'oxhxkbiasqmsfvby'

    msg.attach(MIMEText(html_content, 'html'))

    imagem_anexo = MIMEImage(imagem.read())
    image_name = f'resultado_{client_name.strip().lower().replace(" ", "_")}.jpg'
    imagem_anexo.add_header('Content-Disposition', 'attachment', filename=image_name)
    msg.attach(imagem_anexo)

    try:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()
        print('Email enviado com sucesso')
        return True

    except Exception as e:
        print(f'{e}. Erro ao enviar o email.')
        return False
