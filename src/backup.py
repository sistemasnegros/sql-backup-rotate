# -*- coding: utf-8 -*-

import re
import os


import logging
from subprocess import PIPE, Popen

from lib_sysblack.lib_folder_incremental import folder_incremental

from hurry.filesize import size

from utils import ObjectJS


class Backup(object):
    """Class controllers settings backups"""

    def __init__(self, config, errors):
        self.config = config
        self.errors = errors

    def gen_command_backup(self, config, fecha, hora):
        comando = config.get("GENERAL", "command")

        # search var in text with pattern ${variable}
        patron = re.compile(r'\$\{([^ /]+)\}')

        variables = patron.findall(comando)

        for var in variables:
            valor = config.get("GENERAL", var)

            valor = valor.replace("${date}", fecha)
            valor = valor.replace("${time}", hora)

            comando = comando.replace("${%s}" % var, valor)

        return comando

    def gen_name_file_backup_latest(self, config, fecha, hora):

        name_file_backup_latest = config.get("GENERAL", "namefilebackup")
        name_file_backup_latest = name_file_backup_latest.replace("${date}", fecha)
        name_file_backup_latest = name_file_backup_latest.replace("${time}", hora)

        return name_file_backup_latest

    def run_command_backup(self, config, comando, numbers_backup, path_name_temp, ruta_destino):
        # Object from return only data importain.
        result = ObjectJS()
        log = 'Ejecutando comando...'
        logging.info(log)

        size_dump_file = 0
        error_encontrado = None

        # Check path exist.
        if os.path.exists(ruta_destino):

            proceso = Popen(comando, shell=True, stderr=PIPE)

            error_encontrado = proceso.stderr.read()
            proceso.stderr.close()

            # If not error run command
            if not error_encontrado:
                logging.info('executed command ok.')

                if os.path.exists(path_name_temp):
                    size_dump_file = os.path.getsize(path_name_temp)
                    size_dump_file = size(size_dump_file)

                logging.info('rotations folders backups.')

                # Rotation logs
                folder_incremental(path_name_temp, ruta_destino, numbers_backup, "sql")

            else:
                log = "Error executed command: %s." % error_encontrado
                logging.error(log)
                # Delete file empy.
                os.remove(path_name_temp)

        # if valid path valid.
        else:
            log = "Error, path not access."
            logging.error(log)
            error_encontrado = log

        result.err = error_encontrado
        result.size = size_dump_file
        # return error_encontrado
        return result
