from dataclasses import field
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class create_user(UserCreationForm):
    email = forms.EmailField()
    password1:forms.CharField (label="Contraseña", widget=forms.PasswordInput)
    password2:forms.CharField (label="Repita contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name","password1", "password2"]


class user_editform(UserCreationForm):
    email = forms.EmailField()
    password1:forms.CharField (label="Contraseña", widget=forms.PasswordInput)
    password2:forms.CharField (label="Repita contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name","password1", "password2"]
