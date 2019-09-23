#Sql Backup Rotate

this scritp allow backup sql mysql,postgres,sqlserver ability to rotate in theree backups



#Requeriments
* pip install hurry.filesize
* pip install unipath



### Examples used

#### Mode test pending..
```
$ python main.py -v -d -t
```

#### Mode basic
```
$ python main.py -v
```

#### Mode basic in windows with executable
```:
sql-backup-rotate.exe -v -d
```



#download executable for windows "pending.."
[download.fullkernel.com.co/sql-backup-rotate.exe](http://download.fullkernel.com.co/sql_backup_rotate.exe)


###Loging and debug

```
$ python main.py -d -v -c sql_backup_rotate.cfg.dev
2019-09-23 11:33:07,960 DEBUG: enable mode debuging...
2019-09-23 11:33:07,961 INFO: load file config: sql_backup_rotate.cfg
2019-09-23 11:33:07,961 INFO: executing command...
2019-09-23 11:33:08,399 INFO: executed command ok.
2019-09-23 11:33:08,399 INFO: rotations folders backups.
2019-09-23 11:33:08,400 INFO: not executed command unmount.
2019-09-23 11:33:08,400 INFO: Script teminated.
 ```
