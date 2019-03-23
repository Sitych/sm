from django import forms


class AuthorizationForm(forms.Form):
    login = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
