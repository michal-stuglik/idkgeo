import os
from idkgeo.base import *
import pathlib

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+3!a^x=o%rvvp&=zy9ii9h5cxz9yqwrfw$n2o(x^)3mfgxq7o2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

current_file_path = pathlib.Path(__file__).parent.absolute()
MEDIA_ROOT = str(current_file_path.parent.absolute()) + '/media/'

STATIC_URL = '/static/'

THUMBNAIL_DEBUG = True

SITE_ID = 1
