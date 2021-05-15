# Api

Repositorio de la Api para Ganaderos APP.

# Proceso para compilacion y ejecucion de la Api
## Compilar 

```bash
sudo docker-compose build 
```

## Makemigratios

```bash
sudo docker-compose run --rm api-django python manage.py makemigrations
```

## Migrate

```bash
sudo docker-compose run --rm api-django python manage.py migrate
```

## Create superuser

```bash
sudo docker-compose run --rm api-django python manage.py createsuperuser
```
## parametros a ingresar para crear el super uusuario
```bash
Username (leave blank to use 'root'): admin
Email address: email@example.com
Password: 
Password (again): 
Superuser created successfully.
```

## Run

```bash
sudo docker-compose up
```