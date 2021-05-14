import os

from bsale.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mysql_cymysql',
        'NAME': 'bsale_test',
        'USER': 'root',
        'PASSWORD': 'samanthafox',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
