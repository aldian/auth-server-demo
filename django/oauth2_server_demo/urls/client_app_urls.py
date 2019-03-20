from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path('', include('client_app.urls', namespace='client_app')),
]
