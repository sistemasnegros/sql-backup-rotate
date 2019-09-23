# -*- coding: utf-8 -*-

import os
import shutil


def folder_incremental(path_name_temp, ruta_destino, numero_copias=10, prefijo="bak"):

    numero_copias = range(int(numero_copias))
    ultimo_elemento = numero_copias[-1]

    for iterador in numero_copias:

        # Si el iterado es igual a cero
        # solo se ejecuta una vez
        if iterador == 0:
            # Borro la ultima copia realizada
            delete_ultimate_backup(ruta_destino, numero_copias, prefijo)

        else:
            # Renombre de forma desendente los folder
            rename_folder(ruta_destino, ultimo_elemento, prefijo)

            ultimo_elemento = ultimo_elemento - 1

        # Si el ultimo elemento es igual a cero
        if ultimo_elemento == 0:
            # Creo el la carpeta para el backup mas reciente

            folder_lastest = "%s-%s" % (prefijo, ultimo_elemento)
            folder_lastest = ruta_destino.child(folder_lastest)

            if not os.path.exists(folder_lastest):
                os.mkdir(folder_lastest)

    folder_latest = "%s-%s" % (prefijo, ultimo_elemento)
    folder_latest = ruta_destino.child(folder_latest)

    # Muevo el backup mas reciente a la carpeta nombre cero
    if os.path.exists(path_name_temp):

        shutil.move(path_name_temp, folder_latest)


def rename_folder(ruta_destino, ultimo_elemento, prefijo="bak"):

    folder_last = "%s-%s" % (prefijo, ultimo_elemento - 1)
    folder_last = ruta_destino.child(folder_last)

    folder_current = "%s-%s" % (prefijo, ultimo_elemento)
    folder_current = ruta_destino.child(folder_current)

    # print folder_current

    # print folder_last, folder_current
    # Si no existe la ruta temporal la creo
    if not os.path.exists(folder_last):
        os.mkdir(folder_last)

    os.rename(folder_last, folder_current)


def delete_ultimate_backup(ruta_destino, numero_copias, prefijo="bak"):
    # obtemgo el bombre de la ultima carpeta con la copia disponible

    ruta_temp = "%s-%s" % (prefijo, numero_copias[-1])
    ruta_temp = ruta_destino.child(ruta_temp)

    # print "delete_ultimate_backup ", ruta_temp
    # Si no existe la ruta temporal la creo
    if not os.path.exists(ruta_temp):
        os.mkdir(ruta_temp)

    # Borro la ultima copia realizada
    shutil.rmtree(ruta_temp)
