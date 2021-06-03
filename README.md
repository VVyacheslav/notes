Test task

## Technology stack

Python 3, Django, DRF, celery, docker, PostgreSQL

## Start

```
git clone https://github.com/VVyacheslav/test_task.git
cd testwork-globaldots
```

####  Start tests:
```
make autotests
```
#### Create superuser with login `admin` and password `123`:
```
make create-superuser
```
#### Start server:
```
make runserver
```
or
```
docker-compose up
```
By default, replies at http://0.0.0.0:8080

Admin
-
http://0.0.0.0:8080/admin/
