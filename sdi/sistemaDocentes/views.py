# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView, DetailView, ListView

from sdi.sistemaDocentes.forms import LoginForm

# Create your views here.
from sdi.sistemaDocentes.models import Docente, Facultad, Departamento


class IndexView(View):
    form = None
    message = None
    template = "index.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template, self.get_contex())

    def get_contex(self):
        return {'form': self.form, 'message': self.message}


class LoginView(View):
    form = LoginForm()
    message = None
    template = "login.html"
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            self.message = 'Usuario o password incorrectos'
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {'form': self.form, 'message': self.message}


class LogoutView(RedirectView):
        pattern_name = 'login'

        def get(self, request, *args, **kwargs):
            logout(request)
            return super(LogoutView, self).get(request, *args, **kwargs)


class UnidadesInvestigacionView(LoginRequiredMixin, View):
    form = None
    message = None
    template = "UnidadesInvestigacion/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.get_contex())

    def get_contex(self):
        return {'form': self.form, 'message': self.message}


class FacultadListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Facultad
    template_name = 'UnidadesInvestigacion/facultad.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(FacultadListView, self).get_context_data(
            **kwargs)
        return context


class DepartamentoListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Departamento
    template_name = 'UnidadesInvestigacion/departamento.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListViews, self).get_context_data(
            **kwargs)
        return context


class DocenteListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Docente
    template_name = 'Docentes/docente-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DocenteListViews, self).get_context_data(
            **kwargs)
        return context