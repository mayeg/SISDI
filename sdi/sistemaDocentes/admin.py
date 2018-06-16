# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from sdi.sistemaDocentes.models import *

admin.site.register(Docente)
admin.site.register(Facultad)
admin.site.register(Departamento)
admin.site.register(GrupoInvestigacion)
admin.site.register(SemilleroInvestigacion)
admin.site.register(ProyectoInvestigacion)
admin.site.register(Beneficios)
admin.site.register(Compromiso_Docente)
admin.site.register(TipologiaProductos)
admin.site.register(ClasificacionProductos)
admin.site.register(Lineas_investigacion)
admin.site.register(Titulo_Docente)