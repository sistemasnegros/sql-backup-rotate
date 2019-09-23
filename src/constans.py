# -*- coding: utf-8 -*-
"""this file have all the constan"""

# allow relative path
from unipath import Path

### Only Const  ###

# Name aplication
NAMEAPP = "sql_backup_rotate"

# Raiz del proyecto
PROJECT_DIR = Path(__file__).ancestor(1)


NAME_FILE_LOG = "%s.log" % (NAMEAPP)
NAME_FILE_LOG_PATH = PROJECT_DIR.child(NAME_FILE_LOG)


NAME_FILE_CONFIG = "%s.cfg" % (NAMEAPP)
NAME_FILE_CONFIG_PATH = PROJECT_DIR.child(NAME_FILE_CONFIG)
