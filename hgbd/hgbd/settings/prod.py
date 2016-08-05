# hgbd_project/hgbd/hgbd/settings/prod.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.hgbd.com.ua']

SECRET_KEY = '^!x^wl2__*yo^24pmz(jwu3h8!mw8yc(em*io@ie-zaw9f&tkp'

# Databases

DATABASES['default'].update({
    'HOST':     'localhost',
    'PORT':     '3306',
    'USER':     'hgbd',
    'PASSWORD': 'hgbd',
})
