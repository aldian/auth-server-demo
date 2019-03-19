from django.conf.urls import url
from . import views


app_name = 'client_app'

urlpatterns = [
    url(r'^auth/token/exchange/$', views.AuthTokenExchange.as_view(), name='auth-token-exchange'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
