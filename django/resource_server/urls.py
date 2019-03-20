from django.conf.urls import url
from . import views


app_name = 'resource_server'

urlpatterns = [
    url(r'^resources/$', views.ResourceView.as_view(), name='resources'),
]
