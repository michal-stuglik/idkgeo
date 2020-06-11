## django backend geo server

### conda environment
```
conda env create -f environment.yml
conda activate idkgeo
```
### production with gunicorn
```
gunicorn --env DJANGO_SETTINGS_MODULE=idkgeo.prod idkgeo.wsgi -b unix:/tmp/proxy_geo.dzikiekarpaty.org.sock
```
