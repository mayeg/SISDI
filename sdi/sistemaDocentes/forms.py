from django import forms
from sdi.sistemaDocentes.models import *


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages = {
            'required': 'Debe llenar los campos',
            'invalid': 'Ingrese el nombre de usuario correcto'
    }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={
            'required': 'Debe llenar los campos',
            'invalid': 'Ingrese la contraseña correcta'
        }
    )


class DepartamentoForm(forms.Form):

    class meta:

        model = Departamento
        fields = ['nombre', 'director', 'falcultad']

        widgets = {

            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',
                       }),
            'director': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Director'
                }),
            'falcultad': forms.ModelChoiceField(
                queryset=Facultad.objects.all(),
                empty_label=None
            ),
        }


class GrupoInvestigacionForm(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    estatus = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    horas_recomendadas = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    director = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        label="DIRECTOR", initial="Seleccione un director",
        widget=forms.Select(attrs={
            'class': 'form-control'}),
    )
    facultad = forms.ModelChoiceField(
        queryset=Facultad.objects.all(),
        label="FACULTAD", initial="Seleccione una facultad",
        widget=forms.Select(attrs={
            'class': 'form-control'}),
    )


class SemilleroInvestigacionForm(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    horas_recomendadas = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    director = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        label="DIRECTOR", initial="Seleccione un director",
        widget=forms.Select(attrs={
            'class': 'form-control'}),
    )
    facultad = forms.ModelChoiceField(
        queryset=Facultad.objects.all(),
        label="FACULTAD", initial="Seleccione una facultad",
        widget=forms.Select(attrs={
            'class': 'form-control'}),
    )


class ProyectoInvestigacionForm(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    horas_recomendadas = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    tipo_proyecto = forms.CharField(
        widget=forms.Select(attrs={
            'class': 'form-control', 'placeholder': 'Usuario'}),
        error_messages={
            'required': 'Debe llenar los campos',
        }
    )
    director = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        label="DIRECTOR", initial="Seleccione un director",
        widget=forms.Select(attrs={
            'class': 'form-control'}),
    )
    grupo = forms.ModelChoiceField(
        queryset=GrupoInvestigacion.objects.all(),
        label="GRUPO DE INVESTIGACION", initial="Seleccione un grupo",
        widget=forms.Select(attrs={
            'class': 'form-control'}),
    )