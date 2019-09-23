# -*- coding: utf-8 -*-

import logging
import argparse



class GenericConfig(object):
    """Class contollers load settings file config"""

    def __init__(self, load_config, name_file_config_path, name_file_log_path):
        self.name_file_config_path = name_file_config_path
        self.name_file_log_path = name_file_log_path
        self.args = ""
        self.config = ""
        self.load_config = load_config

    def loading_args(self):
        """Argumento de ejecucion"""

        parser = argparse.ArgumentParser()
        parser.add_argument("-v", "--verbose", help="Mostrar información en consola.", action="store_true")
        parser.add_argument("-c", "--config", help="Nombre de archivo de configuracion.", default=self.name_file_config_path)
        parser.add_argument("-d", "--debug", help="Mostrar información de depuración.", action="store_true")
        #parser.add_argument("-t", "--test", help="Tirar una prueba del comando.", action="store_true")

        self.args = parser.parse_args()

    def log_configuration(self):
        """config settings logs"""

        level_log = logging.INFO

        if self.args.debug:
            level_log = logging.DEBUG

        logformat = "%(asctime)s %(levelname)s: %(message)s"

        logging.basicConfig(filename=self.name_file_log_path, filemode='w', format=logformat, level=level_log)

        if self.args.verbose:
            stream_handler = logging.StreamHandler()
            log_formatter = logging.Formatter(logformat)
            stream_handler.setFormatter(log_formatter)
            logging.getLogger().addHandler(stream_handler)

        logging.debug("enable mode debuging...")

    def loading_file_config(self):
        """load file config"""
        return self.load_config(self.args.config)
