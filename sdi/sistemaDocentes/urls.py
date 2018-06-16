from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [

    path('login', views.LoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('docente/list', views.DocenteListViews.as_view(), name='docente-list'),
    path('unidadInvestigacion', views.UnidadesInvestigacionView.as_view(), name='unidadInvestigacion'),
    path('facultad', views.FacultadListView.as_view(), name='facultad'),
    path('facultad/crear', views.FacultadCreateView.as_view(), name='facultad-crear'),
    path('departamento', views.DepartamentoListViews.as_view(), name='departamento'),
    path('departamento/crear', views.DepartamentoCreateViews.as_view(), name='departamento-crear'),
    path('grupos', views.GruposListViews.as_view(), name='grupos'),
    path('grupos/crear', views.GrupoInvestigacionCreateViews.as_view(), name='grupo-crear'),
    path('semilleros', views.SemilleroListViews.as_view(), name='semilleros'),
    path('semilleros/crear', views.SemilleroInvestigacionCreateViews.as_view(), name='semillero-crear'),
    path('proyecto', views.ProyectoListViews.as_view(), name='proyecto'),
    path('proyecto/crear', views.ProyectoInvestigacionCreateViews.as_view(), name='proyecto-crear'),
]
