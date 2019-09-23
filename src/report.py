# -*- coding: utf-8 -*-
import string


def gen_report(DATE, HORA_INICIO, HORA_FINAL, PATH, SIZE, ERROR):
    remplace_vars = {
        "DATE": DATE,
        "HORA_INICIO": HORA_INICIO,
        "HORA_FINAL": HORA_FINAL,
        "PATH": PATH,
        "SIZE": SIZE,
        "ERROR": ERROR,
    }

    with open("email.html", "r") as template:
        template_readed = template.read()
        template_readed = string.Template(template_readed)
        template_readed = template_readed.substitute(**remplace_vars)

    return template_readed
