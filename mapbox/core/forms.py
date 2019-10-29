from django import forms

from django.contrib.auth.models import User
from accounts.models import *

class NovoUsuario(forms.Form):
    username = forms.TextField(User, on_delete=models.CASCADE)
    name = forms.EmailField()
    email = forms.EmailField(max_length=30, blank=True)
    senha = forms.PasswordInput(null=True, blank=True)