from django import forms
from sdi.sistemaDocentes.models import *


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Contraseña'}),
    )


class DepartamentoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Nombre'})
    )
    codigo = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'codigo'})
    )
    director = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Director'})
    )
    falcultad = forms.Select()
