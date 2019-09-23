# -*- coding: utf-8 -*-

import logging
# allow send email in an easy way
from lib_sysblack.lib_mail import send_mail


class Mail(object):
    """class controllers settings mail and send"""

    def __init__(self, config, NAME_FILE_LOG_PATH):
        super(Mail, self).__init__()
        # self.arg = arg
        self.is_enable = config.get("MAIL", "enable")
        self.send_from = config.get("MAIL", "send_from")
        self.username = config.get("MAIL", "username")
        self.password = config.get("MAIL", "password")
        self.send_to = config.get("MAIL", "send_to")
        self.files = config.get("MAIL", "files")
        if self.files == "no":
            self.files = None

        self.server = config.get("MAIL", "server")
        self.port = config.get("MAIL", "port")
        self.tls = config.get("MAIL", "tls")

        self.NAME_FILE_LOG_PATH = NAME_FILE_LOG_PATH

        self.subject_error = config.get("MAIL", "subject_error")
        self.subject_ok = config.get("MAIL", "subject_ok")

    def check_enable(self):
        """check if option mail is enable"""
        return self.is_enable == "yes"

    def fun_send_mail(self, report=False):
        """funtion that make send email in an easy way"""
        if self.check_enable():

            with open(self.NAME_FILE_LOG_PATH) as my_file:
                data_log = my_file.read()

            if data_log.find("ERROR") != -1:
                subject = self.subject_error
            else:
                subject = self.subject_ok

            if not report:
                report = data_log

            for email in self.send_to.split(","):

                try:
                    send_mail(
                        self.username,
                        self.password,
                        self.send_from,
                        email.strip(),
                        subject,
                        report,
                        self.files,
                        self.server,
                        self.port,
                        self.tls
                    )

                    logging.info('send email ok.')

                except Exception as e:
                    # raise e
                    log = "Al Enviar email: {}.".format(e)
                    logging.error(log)
