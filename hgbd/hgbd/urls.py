# hgbd_project/hgbd/hgbd/urls.py
from django.conf.urls import include, url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

from solid_i18n.urls import solid_i18n_patterns

from .admin import admin_site

handler400 = 'website.views.handler400'
handler403 = 'website.views.handler403'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'

urlpatterns = [
    url(r'^deus_ex_machina/', admin_site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += solid_i18n_patterns(
    url(r'', include('website.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
