# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import sys

import logging


def load_config(name_file):
    config = ConfigParser()

    if config.read(name_file) == []:
        ERROR_LOAD_CONFIG = "No se puedo cargar el archivo de configuracion: {}"
        logging.error(ERROR_LOAD_CONFIG.format(name_file))

        # print ERROR_LOAD_CONFIG.format(name_file)
        sys.exit(0)

    else:
        INFO_LOAD_CONFIG = "Cargado archivo de configuracion: {}"
        logging.info(INFO_LOAD_CONFIG.format(name_file))
        return config
