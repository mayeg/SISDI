# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from builtins import print, Exception

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import RedirectView, DetailView, ListView, CreateView

from sdi.sistemaDocentes.forms import LoginForm, DepartamentoForm
from django.contrib import messages
# Create your views here.
from sdi.sistemaDocentes.models import Docente, Facultad, Departamento, GrupoInvestigacion, SemilleroInvestigacion, \
    ClasificacionProductos, ProyectoInvestigacion


class IndexView(LoginRequiredMixin, View):
    form = None
    message = None
    template = "index.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template, self.get_context())

    def get_context(self):
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
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {'form': self.form, 'message': self.message}


class FacultadListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Facultad
    template_name = 'UnidadesInvestigacion/facultad/facultad.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(FacultadListView, self).get_context_data(
            **kwargs)
        return context


class FacultadCreateView(LoginRequiredMixin, CreateView):
    model = Facultad
    fields = '__all__'
    template_name = 'UnidadesInvestigacion/facultad/crear.html'
    success_url = reverse_lazy('facultad')
    login_url = 'login'

    def form_valid(self, form):
        try:
            messages.success(
                self.request, 'Facultad creado correctamente.'
            )
            return super(FacultadCreateView, self).form_valid(form)
        except Exception as e:
            print(e)
            return super(FacultadCreateView, self).form_invalid(form)

    def get_success_url(self):
        depart = self.object.id
        return reverse_lazy('depart', kwargs={'id_dep': depart})


class DepartamentoListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Departamento
    template_name = 'UnidadesInvestigacion/departamento/departamento.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListViews, self).get_context_data(
            **kwargs)
        return context


class DepartamentoCreateViews(LoginRequiredMixin, CreateView):

    model = Departamento
    fields = '__all__'
    template_name = 'UnidadesInvestigacion/departamento/crear.html'
    success_url = reverse_lazy('departamento')
    login_url = 'login'

    def form_valid(self, form):
        try:
            messages.success(
                self.request, 'Departamento creado correctamente.'
            )
            return super(DepartamentoCreateViews, self).form_valid(form)
        except Exception as e:
            print(e)
            return super(DepartamentoCreateViews, self).form_invalid(form)

    def get_success_url(self):
        depart = self.object.id
        return reverse_lazy('departamento', kwargs={'id_dep': depart})


class DocenteListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Docente
    template_name = 'Docentes/docente-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DocenteListViews, self).get_context_data(
            **kwargs)
        return context


class GruposListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = GrupoInvestigacion
    template_name = 'UnidadesInvestigacion/grupo/grupo.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(GruposListViews, self).get_context_data(
            **kwargs)
        return context


class GrupoInvestigacionCreateViews(LoginRequiredMixin, CreateView):

    model = GrupoInvestigacion
    fields = ['nombre', 'estatus', 'horas_recomendadas', 'director', 'facultad']
    template_name = 'UnidadesInvestigacion/grupo/crear.html'
    success_url = reverse_lazy('grupos')
    login_url = 'login'

    def form_valid(self, form):
        try:
            messages.success(
                self.request, 'Grupo de investigacion creado correctamente.'
            )
            return super(GrupoInvestigacionCreateViews, self).form_valid(form)
        except Exception as e:
            print(e)
            return super(GrupoInvestigacionCreateViews, self).form_invalid(form)

    def get_success_url(self):
        grupo = self.object.id
        return reverse_lazy('grupos', kwargs={'id_grup': grupo})


class ClasificacionListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ClasificacionProductos
    template_name = 'Clasificacion/clasificacion.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ClasificacionListViews, self).get_context_data(
            **kwargs)
        return context


class SemilleroListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = SemilleroInvestigacion
    template_name = 'UnidadesInvestigacion/semillero/semillero.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SemilleroListViews, self).get_context_data(
            **kwargs)
        return context


class SemilleroInvestigacionCreateViews(LoginRequiredMixin, CreateView):

    model = SemilleroInvestigacion
    fields = ['nombre', 'horas_recomendadas', 'director', 'facultad']
    template_name = 'UnidadesInvestigacion/semillero/crear.html'
    success_url = reverse_lazy('semilleros')
    login_url = 'login'

    def form_valid(self, form):
        try:
            messages.success(
                self.request, 'Semillero de investigacion creado correctamente.'
            )
            return super(SemilleroInvestigacionCreateViews, self).form_valid(form)
        except Exception as e:
            print(e)
            return super(SemilleroInvestigacionCreateViews, self).form_invalid(form)

    def get_success_url(self):
        semillero = self.object.id
        return reverse_lazy('semilleros', kwargs={'id_semillero': semillero})


class ProyectoListViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = ProyectoInvestigacion
    template_name = 'UnidadesInvestigacion/proyecto/proyecto.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ProyectoListViews, self).get_context_data(
            **kwargs)
        return context


class ProyectoInvestigacionCreateViews(LoginRequiredMixin, CreateView):

    model = ProyectoInvestigacion
    fields = ['nombre', 'horas_recomendadas', 'tipo_proyecto', 'director', 'grupo']
    template_name = 'UnidadesInvestigacion/proyecto/crear.html'
    success_url = reverse_lazy('proyecto')
    login_url = 'login'

    def form_valid(self, form):
        try:
            messages.success(
                self.request, 'Proyecto de investigacion creado correctamente.'
            )
            return super(ProyectoInvestigacionCreateViews, self).form_valid(form)
        except Exception as e:
            print(e)
            return super(ProyectoInvestigacionCreateViews, self).form_invalid(form)

    def get_success_url(self):
        proyecto = self.object.id
        return reverse_lazy('proyecto', kwargs={'id_proyecto': proyecto})
