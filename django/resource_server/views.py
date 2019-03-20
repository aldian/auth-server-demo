from django.conf import settings
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import OAuth2IntrospectionAuthentication


class ResourceView(APIView):
    authentication_classes = (OAuth2IntrospectionAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        return Response(settings.RESOURCE_SERVER_NAME)
