from django.urls import path

from .views import WebsiteDetailListApiView

urlpatterns = [
    path('web_master_details', WebsiteDetailListApiView.as_view()),
]