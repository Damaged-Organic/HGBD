# hgbd_project/hgbd/website/admin.py
from django import forms
from django.contrib import admin

from transmeta import canonical_fieldname

from hgbd.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin, ForbidDeleteMixin,
)


class ContentBlockMixin(ForbidDeleteMixin, ForbidAddMixin):
    exclude = ('name',)
