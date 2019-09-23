# -*- coding: utf-8 -*-

import os
import logging

# Falta desarollar la compatibilidad con linux


def mount_und(**kwargs):
    """list vars: , username_und, password_und, path_network, letter_und """

    username_und = kwargs.pop("username_und")
    password_und = kwargs.pop("password_und")
    path_network = kwargs.pop("path_network")
    destiny_path = kwargs.pop("destiny_path")
    letter_und = kwargs.pop("letter_und")

    #comando_montar_red = "net use %s %s %s /user:%s" % (letter_und, path_network, password_und, username_und)

    if os.name == 'nt':
        # Windows
        comando_montar_red = "net use %s %s %s /user:%s" % (letter_und, path_network, password_und, username_und)
    else:
        # Linux
        comando_montar_red = \
            "mount -t cifs -o username=%s,password=%s,rw,auto,users,exec,uid=1000,gid=1000 %s %s" % (username_und, password_und, path_network, destiny_path)

    return comando_montar_red
    # if not os.path.exists(destiny_path):
    #     return comando_montar_red
    # else:
    #     return


def umount_und(letter_und, destiny_path):
    """Desmonta la unidad"""

    """
    
    umount -f

    net use J: /delete /Y

    """

    if os.name == 'nt':
        # Windows
        comando = "net use %s /delete /Y " % (letter_und)
    else:
        # Linux
        comando = "umount -f %s" % (destiny_path)

    return comando
