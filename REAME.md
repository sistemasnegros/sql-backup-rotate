#Sql Backup Rotate

this scritp allow backup sql mysql,postgres,sqlserver ability to rotate in theree backups



#Requeriments
* pip install lib_sysblack
* pip install hurry.filesize
* pip install unipath



### Examples used

#### mode test
```
$ python main.py -v -d -t
```

#### mode basic
```
$ python main.py -v
```

#### mode basic in windows with executable
```:
sql-backup-rotate.exe -v -d
```



#download executable for windows "pending.."
[download.fullkernel.com.co/sql-backup-rotate.exe](http://download.fullkernel.com.co/sql_backup_rotate.exe)


###Loging and debug

```
$ python main.py -v -t -c sql_backup_rotate.cfg
2018-08-06 09:47:19,900 INFO: Cargado archivo de configuracion: sql_backup_rotate.cfg.dev
2018-08-06 09:47:19,900 INFO: Comando Generado: mysqldump --user=myuser --password=mypassword --single-transaction --skip-opt --add-drop-table --add-locks --create-options --disable-keys --extended-insert --quick --set-charset --databases nodejs | gzip > /tmp/testing/data_sql_2018-08-06--09-47-19.gz
2018-08-06 09:47:19,901 INFO: Ejecutando comando...
2018-08-06 09:47:19,958 INFO: Comando ejecutado exitosamente.
2018-08-06 09:47:19,958 INFO: Rotando backups.
2018-08-06 09:47:19,961 INFO: Script Completado.

```
