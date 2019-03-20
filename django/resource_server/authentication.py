import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions


User = get_user_model()


class OAuth2IntrospectionAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        response = requests.post(settings.AUTH_SERVER_INTROSPECTION_URL, {
            "token": key
        }, headers={
            "Authorization": "{} {}".format(self.keyword, key)
        })
        try:
            response.raise_for_status()
        except:
            raise exceptions.AuthenticationFailed(response.content.decode('utf-8'))

        user_info = response.json()
        user, __ = User.objects.get_or_create(username=user_info['username'])

        return (user, key)
