# -*- coding: utf-8 -*-

# import lin systems
import argparse
import logging
import sys

# allow send email in an easy way
from lib_sysblack.lib_mail import send_mail
# lib manage for mount und samba
from lib_sysblack.lib_mount import mount_und, umount_und
# lib run command
from lib_sysblack.lib_command import run_command


# import const
from constans import NAME_FILE_LOG_PATH, NAME_FILE_CONFIG_PATH


class Mount(object):
    """manage mount point remote"""

    def __init__(
        self,
        errors,
        mount_is_enable,
        umount_is_enable,
        username_und,
        password_und,
        path_network,
        letter_und,
        destiny_path
    ):

        self.errors = errors
        self.mount_is_enable = mount_is_enable
        self.umount_is_enable = umount_is_enable
        self.destiny_path = destiny_path
        self.username_und = username_und
        self.password_und = password_und
        self.path_network = path_network
        self.letter_und = letter_und

    def fun_mount_und(self):
        salida_error_cmd = None
        salida_cmd = None

        if self.mount_is_enable:
            logging.info('enable mount und network.')

            comando = mount_und(
                username_und=self.username_und,
                password_und=self.password_und,
                path_network=self.path_network,
                destiny_path=self.destiny_path,
                letter_und=self.letter_und
            )

            logging.info('Command generated:')

            if comando:
                logging.info(comando)
                salida_error_cmd, salida_cmd = run_command(comando)

                if salida_error_cmd:
                    self.errors.append(salida_error_cmd)

            else:
                log = "error genrating command."
                logging.error(log)
                self.errors.append(log)

        return self.errors, salida_error_cmd, salida_cmd

    def fun_umount(self):
        comando = None
        if self.mount_is_enable and self.umount_is_enable:
            comando = umount_und(self.letter_und, self.destiny_path)

        if comando:
            logging.info(comando)
            run_command(comando)
            log = "executed command unount."

        else:
            log = "not executed command unmount."
            logging.info(log)
            #self.errors.append(log)

        return self.errors
