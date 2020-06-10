### django backend geo server

```
python manage.py makemigrations geo
python manage.py migrate
```

### production
```
gunicorn --env DJANGO_SETTINGS_MODULE=idkgeo.prod idkgeo.wsgi -b :8002
# gunicorn --env DJANGO_SETTINGS_MODULE=idkgeo.prod idkgeo.wsgi -b unix:${HOME}/gunicorn.socket
```


### ref
[easy-thumbnails](https://pypi.org/project/easy-thumbnails/)