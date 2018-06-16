# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Facultad(models.Model):
    nombre = models.CharField(max_length=250)
    decano = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Departamento(models.Model):
    nombre = models.CharField(max_length=250)
    director = models.CharField(max_length=50, unique=True)
    falcultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return u'{0}'.format(self.nombre)

class Beneficios(models.Model):
    TIPO_BENEFICIO_CHOICES = (
        ('movilidad_internacional', 'Movilidad internacional'),
        ('movilidad_nacional', ' Movilidad nacional '),
        ('diplomado ', 'Diplomado')
    )
    TIEMPO_CHOICES = (
        ('año(s)', 'Año(s)'),
        ('mes(s)', 'Mes(s)'),
        ('dia(s)', 'Dia(s)')
    )
    tipo = models.CharField(max_length=50, choices=TIPO_BENEFICIO_CHOICES,
                                        default='No seleccion')
    descripcion = models.CharField(max_length=350)
    plazo_entrega = models.IntegerField()
    tiempo = models.CharField(max_length=50, choices=TIEMPO_CHOICES,
                            default='No seleccion')

    def __str__(self):
        return u'{0}'.format(self.tipo)


class ClasificacionProductos(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=350)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class TipologiaProductos(models.Model):
    nombre = models.CharField(max_length=350)
    clasificacion = models.ForeignKey(ClasificacionProductos, on_delete=models.CASCADE)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Titulo_Docente(models.Model):
    NIVEL_FORMACION_CHOICES = (
        ('tecnologia','Tecnologia'),
        (' pregrado ', ' Pregrado '),
        (' especializacion ', ' Especializacion '),
        (' maestria ', ' Maestria '),
        (' doctorado ', ' Doctorado '),
        ('phd', 'PhD'),
    )
    nombre = models.CharField(max_length=255, unique=True)
    nivel_formacion = models.CharField(max_length=50, choices=NIVEL_FORMACION_CHOICES,
                                        default='No seleccion')

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Lineas_investigacion(models.Model):
    nombre = models.CharField(max_length=350)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Docente(models.Model):
    TIPO_VINCULACION_CHOICES = (
        (' Catedra', 'Catedra'),
        (' Planta', 'Planta'),
        (' Ocacional', ' Ocacional'),
    )
    REPRESENTANTE_FACULTAD_INVESTIGACION_CHOICES = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    cedula = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    titulo = models.ManyToManyField(Titulo_Docente)
    tipo_vinculacion = models.CharField(max_length=50, choices=TIPO_VINCULACION_CHOICES,
                                        default='No seleccion')
    facultad = models.ForeignKey(Facultad, null=True, blank=True,
                                 on_delete=models.CASCADE)
    representante_facultad_investigacion = models.CharField(max_length=2, choices=REPRESENTANTE_FACULTAD_INVESTIGACION_CHOICES,
                                                            default='No seleccion')

    def __str__(self):
        return u'{0}'.format(self.nombre)


class Compromiso_Docente(models.Model):
    docente_id = models.ForeignKey(Docente, on_delete=models.CASCADE)
    tipologia_id = models.ForeignKey(TipologiaProductos, on_delete=models.CASCADE)
    beneficios_id = models.ForeignKey(Beneficios, on_delete=models.CASCADE)
    archivo = models.FileField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return u'{0}'.format(self.docente_id.attname)


class GrupoInvestigacion(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    estatus = models.CharField(max_length=50)
    horas_recomendadas = models.CharField(max_length=50)
    director = models.OneToOneField(Docente, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, null=True, blank=True,
                                 on_delete=models.CASCADE)
    lineas_investigacion = models.ManyToManyField(Lineas_investigacion)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class SemilleroInvestigacion(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    horas_recomendadas = models.CharField(max_length=50)
    director = models.OneToOneField(Docente, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, null=True, blank=True,
                                 on_delete=models.CASCADE)
    lineas_investigacion = models.ManyToManyField(Lineas_investigacion)

    def __str__(self):
        return u'{0}'.format(self.nombre)


class ProyectoInvestigacion(models.Model):

    TIPO_PROYECTO_CHOICES = (
        ('proyecto_investigacion', 'Proyecto de investigacion'),
        ('proyecto_investigacion_institucional', 'Proyecto de investigacion institucional'),
        ('proyecto_investigacion_interno', 'Proyecto de investigacion interno'),
    )
    nombre = models.CharField(max_length=250, unique=True)
    horas_recomendadas = models.CharField(max_length=50)
    tipo_proyecto = models.CharField(max_length=150, choices=TIPO_PROYECTO_CHOICES,
                                     default='No seleccion')
    director = models.OneToOneField(Docente, related_name='+', on_delete=models.CASCADE)
    grupo = models.OneToOneField(GrupoInvestigacion, related_name='+', on_delete=models.CASCADE)
    coinvestigador = models.ManyToManyField(Docente, related_name='+')
    tutor = models.OneToOneField(Docente, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    joven_investigador = models.CharField(max_length=150, null=True)

    def __str__(self):
        return u'{0}'.format(self.nombre)

#----- Beneficios y compromisos, tipologia de productos
