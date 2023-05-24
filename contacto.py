#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getenv
import cgi


# IP o dirección del servidor SMTP.
SMTP_SERVER = "smtp.[...].com"
# Puerto.
SMTP_PORT = 465
# Dirección desde donde se envía el correo.
EMAIL_ADDRESS = "[...]@[...].com"
# Constraseña.
PASSWORD = "********"
# Dirección a la que se envía el correo (usualmente igual a EMAIL_ADDRESS).
RECEIVER = "[...]@[...].com"

# Datos reCAPTCHA: clave del sitio y secreta.
PUBLIC_KEY = "[...]"
SECRET_KEY = "[...]"

# Código HTML del formulario.
FORM_HTML_CODE = \
"""
<form method="post">
  Nombre:<br /><input name="name" type="text" /><br />
  Email:<br /><input name="email" type="text" /><br />
  Mensaje:<br /><textarea name="message"></textarea><br />
  Verificación:<br />
  <div class="g-recaptcha" data-sitekey="{public_key}"></div>
  <br />
  <button type="submit">Enviar</button>
</form>
"""


def body():
    if getenv("REQUEST_METHOD") == "GET":
        # Mostrar formulario.
        print(FORM_HTML_CODE.format(public_key=PUBLIC_KEY))
    else:
        # Enviar formulario.
        form_input = cgi.FieldStorage()
        required_fields = ("name", "email", "message",
                           "g-recaptcha-response")
        for field in required_fields:
            if field not in form_input:
                print("Debes completar todos los campos.")
                return
        
        # Verificar reCAPTCHA.
        import requests
        result = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": SECRET_KEY,
                "response": form_input["g-recaptcha-response"].value,
                "remote-ip": getenv("REMOTE_ADDR")
            }
        )
        success = result.json()["success"]
        if not success:
            print("Realice nuevamente la verificación de seguridad.")
            return
        
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from smtplib import SMTP, SMTP_SSL
        
        mime_message = MIMEMultipart("alternative")
        mime_message["From"] = EMAIL_ADDRESS
        mime_message["To"] = RECEIVER
        mime_message["Subject"] = "Formulario de contacto"
        
        text = "Nombre: {}\nEmail: {}\n\n{}".format(
            form_input["name"].value,
            form_input["email"].value,
            form_input["message"].value
        )
        
        text = MIMEText(text, "plain", _charset="utf-8")
        mime_message.attach(text)
        
        # Iniciar sesión.
        smtp = SMTP(SMTP_SERVER, SMTP_PORT)
        # O bien la siguiente línea en lugar de la anterior
        # para conexiones seguras.
        # smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(EMAIL_ADDRESS, PASSWORD)
        
        # Enviar correo.
        smtp.sendmail(EMAIL_ADDRESS, RECEIVER, mime_message.as_string())
        smtp.quit()
        
        print("¡Tu mensaje ha sido enviado!")


def main():
    # Headers.
    print ("Content-Type: text/html")
    print
    
    print ("""\
    <html>
    <head>
      <title>Formulario de contacto</title>
      <meta http-equiv="content-type" content="text/html;charset=utf-8" />
      <script src='https://www.google.com/recaptcha/api.js'></script>
    </head>
    <body>
      <h3>Contacto</h3>""")
    
    body()
    
    print ("</body></html>")


if __name__ == "__main__":
    main()
