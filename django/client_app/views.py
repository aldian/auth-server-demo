import logging

import requests
from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import RedirectView, TemplateView

from . import forms

log = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'client_app/home.html'

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        data = self.request.POST or {}
        if not data.get('access_token'):
            data['access_token'] = self.request.session.get('access_token', '')
        if not data.get('resource_server_1_path'):
            data['resource_server_1_path'] = '/resources/'
        if not data.get('resource_server_2_path'):
            data['resource_server_2_path'] = '/resources/'
        form = forms.ResourceAccessForm(data)

        context = super().get_context_data(**kwargs)
        context.update(dict(
            authorization_url='{}?client_id={}&response_type=code'.format(
                settings.AUTH_SERVER_AUTHORIZE_URL,
                settings.CLIENT_ID,
            ),
            form=form,
            response_content_1=self.request.session.get('response_content_1', '-'),
            response_content_2=self.request.session.get('response_content_2', '-'),
        ))
        return context

    def post(self, request, *args, **kwargs):
        form = forms.ResourceAccessForm(request.POST)
        if form.is_valid():
            response = requests.get(urljoin(
                settings.RESOURCE_SERVER_1_BASE_URL,
                request.session.get('resource_server_1_path', form.cleaned_data['resource_server_1_path'])
            ), headers={"Authorization": "Bearer {}".format(form.cleaned_data['access_token'])})
            request.session['response_content_1'] = "{} {}".format(
                response.status_code, response.content.decode('utf-8')
            )

            response = requests.get(urljoin(
                settings.RESOURCE_SERVER_2_BASE_URL,
                request.session.get('resource_server_2_path', form.cleaned_data['resource_server_2_path'])
            ), headers={"Authorization": "Bearer {}".format(form.cleaned_data['access_token'])})
            request.session['response_content_2'] = "{} {}".format(
                response.status_code, response.content.decode('utf-8')
            )
            return HttpResponseRedirect(reverse('client_app:home'))

        return render(request, self.template_name, self.get_context_data())


class AuthTokenExchange(RedirectView):
    url = reverse_lazy('client_app:home')

    def get(self, request, *args, **kwargs):
        response = requests.post(settings.AUTH_SERVER_TOKEN_URL, dict(
            code=request.GET.get('code'),
            client_id=settings.CLIENT_ID,
            client_secret=settings.CLIENT_SECRET,
            grant_type='authorization_code',
        ))
        response.raise_for_status()
        tokens = response.json()
        request.session['access_token'] = tokens["access_token"]
        return super().get(request, *args, **kwargs)
