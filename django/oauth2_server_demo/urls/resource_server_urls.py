from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path('', include('resource_server.urls', namespace='resource_server')),
]
