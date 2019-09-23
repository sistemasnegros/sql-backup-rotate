# -*- coding: utf-8 -*-


import subprocess
import logging


def run_command(comando):
    logging.info('Ejecutando el comando generado.')
    sp = subprocess.Popen(comando.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida_cmd = sp.stdout.read()
    salida_error_cmd = sp.stderr.read()
    sp.stdout.close()
    sp.stderr.close()

    if salida_error_cmd != "":
        logging.error("Al ejecutar comando: {}.".format(comando))
        logging.error(salida_error_cmd)

    if salida_cmd:
        logging.info('Comando ejecutado saticfactoriamente: {}.'.format(comando))
        logging.debug(salida_cmd)

    return salida_error_cmd, salida_cmd
