# hgbd_project/hgbd/hgbd/settings/dev.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = 'Something secret steers at us!'

INSTALLED_APPS += [
    'debug_toolbar',
]

# Databases

DATABASES['default'].update({
    'HOST':     'localhost',
    'PORT':     '3306',
    'USER':     'hgbd',
    'PASSWORD': 'hgbd',
})
