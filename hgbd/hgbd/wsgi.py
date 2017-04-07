# hgbd_project/hgbd/hgbd/wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hgbd.settings.dev")

application = get_wsgi_application()
