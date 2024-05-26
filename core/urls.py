from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from web_master_api import urls as web_master_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('custom_admin.urls')),
    path('api/', include(web_master_urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
