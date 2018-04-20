# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import View

from sdi.sistemaDocentes.forms import LoginForm

# Create your views here.


class LoginView(View):
    form = LoginForm()
    message = None
    template = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.get_contex())

    def get_contex(self):
        return {'form': self.form, 'message': self.message}