from django import forms


class ResourceAccessForm(forms.Form):
    access_token = forms.CharField(label='Access Token', max_length=100)
    resource_server_1_path = forms.CharField(label='From Resource Server 1', max_length=300)
    resource_server_2_path = forms.CharField(label='From Resource Server 2', max_length=300)
