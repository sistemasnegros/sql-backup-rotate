# -*- coding: utf-8 -*-
"""
Fuction Main
"""
# lib system
import time
import datetime
import os
import logging
# from subprocess import PIPE, Popen

# lib the trird-partys
# from hurry.filesize import size
from unipath import Path
from hurry.filesize import size
# allow redunt folder for backup
# from lib_sysblack.lib_folder_incremental import folder_incremental

# load file config .cfg
from lib_sysblack.lib_config import load_config


# from basicFunction import *

# from command_backup import gen_command_backup


# import functions locals
from constans import NAME_FILE_LOG_PATH, NAME_FILE_CONFIG_PATH


from generic import GenericConfig
from report import gen_report
from backup import Backup
from mail import Mail

from mount import Mount


class Main(GenericConfig):
    """docstring for Main"""

    def __init__(self):
        super(Main, self).__init__(load_config, NAME_FILE_CONFIG_PATH, NAME_FILE_LOG_PATH)

        self.loading_args()
        self.log_configuration()

        # General
        self.config = self.loading_file_config()
        self.errors = []

        self.fecha = str(datetime.date.today())
        self.hora_inicio = str(time.strftime("%H-%M-%S"))
        self.numbers_backup = self.config.get("GENERAL", "numbers_backup")
        self.ruta_destino = Path(self.config.get("GENERAL", "destiny_path"))

        # Mount and unmount
        self.mount_is_enable = self.config.get("MOUNT", "enable") == "yes"
        self.umount_is_enable = self.config.get("MOUNT", "umount") == "yes"
        self.username_und = self.config.get("MOUNT", "username_und")
        self.password_und = self.config.get("MOUNT", "password_und")
        self.path_network = self.config.get("MOUNT", "path_network")
        self.letter_und = self.config.get("MOUNT", "letter_und")

        self.mount = Mount(
            self.errors,
            self.mount_is_enable,
            self.umount_is_enable,
            self.username_und,
            self.password_und,
            self.path_network,
            self.letter_und,
            self.ruta_destino
        )

        # Run command mount und network
        errors, salida_error_cmd, salida_cmd = self.mount.fun_mount_und()
        self.errors = errors

        # Backups
        self.backup = Backup(self.config, self.errors)
        self.command_backup = self.backup.gen_command_backup(self.config, self.fecha, self.hora_inicio)
        self.name_file_backup_latest = self.backup.gen_name_file_backup_latest(self.config, self.fecha, self.hora_inicio)

        # gen path temp Backup
        self.path_name_temp = self.ruta_destino.child(self.name_file_backup_latest)

        size_dump_file = 0


        # Is not errors in mounting
        if not self.errors:
            result = self.backup.run_command_backup(
                self.config,
                self.command_backup,
                self.numbers_backup,
                self.path_name_temp,
                self.ruta_destino,
            )

            size_dump_file = result.size
            self.errors = result.err

        full_path_dump = self.ruta_destino + "/sql-0/" + self.name_file_backup_latest

        # unmount if mount
        self.mount.fun_umount()

        hora_final = time.strftime("%H-%M-%S")

        report = gen_report(self.fecha, self.hora_inicio, hora_final, full_path_dump, size_dump_file, self.errors)

        # Function send notification.
        mail = Mail(self.config, NAME_FILE_LOG_PATH)
        mail.fun_send_mail(report)

        logging.info("Script Completado.")


if __name__ == '__main__':
    main = Main()
