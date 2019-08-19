# Cómo contribuir con Loiprocesos.


## Deploy en Heroku
Es necesario tener instalado y configurado Heroku. Seguir
[el tutorial de Fisa](https://github.com/fisadev/docs/blob/master/django_heroku.rst) como 
referencia.
Los comandos para deployar son:
```
git push heroku master
heroku run "python manage.py migrate"
```

## Backup de la base de datos
Heroku nos provee una forma fácil para generar un backup del postgresql que está en producción.
Con el siguiente comando se crea un archivo de backup de la db:
```
heroku pg:backups:capture
```
Y con este comando se descarga en el backup en un archivo llamado `latest.dump`
```
heroku pg:backups:download
```
Una vez descargado el archivo se puede cargar a la base de datos postgresql local de la siguiente
manera:
```
pg_restore --verbose --clean --no-acl --no-owner -h localhost -U [USER_NAME] -d [SCHEMA_NAME] latest.dump
```
Reemplazando [USER_NAME] y [SCHEMA_NAME] por los datos correspondientes.
