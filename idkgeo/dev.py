import os
from idkgeo.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+3!a^x=o%rvvp&=zy9ii9h5cxz9yqwrfw$n2o(x^)3mfgxq7o2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# STATIC_URL = '/uploads/'

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
# )
#
# STATIC_ROOT = ''
MEDIA_ROOT = '/home/michal/workspace/code/idkgeo/media/'
# MEDIA_UPLOAD = 'uploads/'

STATIC_URL = '/static/'

THUMBNAIL_DEBUG = True

# SITE_URL = 'http://127.0.0.1:8002/'

SITE_ID = 1