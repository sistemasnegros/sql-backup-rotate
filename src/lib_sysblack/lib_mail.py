# -*- coding: utf-8 -*-
"""Este modulo se encarga de mandar emails con datos"""

# Libreria
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
#from email.utils import COMMASPACE, formatdate

import smtplib

import logging


def send_mail(username, password, send_from, send_to, subject, text, files=None, server="127.0.0.1", port=25, tls=False):
    """send email"""

    msg = MIMEMultipart()
    msg['From'] = send_from
    #msg['To'] = COMMASPACE.join(send_to)
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    for f in files or []:

        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    servidor_puerto = "%s:%s" % (server, port)

    smtp = smtplib.SMTP(servidor_puerto)

    if tls:
        smtp.starttls()

    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
