# -*- coding: utf-8 -*-
import os
import csv

from django.core.management.base import BaseCommand, CommandError

from sdi.sistemaDocentes.models import Docente, Titulo_Docente

CODIGO_FIELD = "CODIGO"
DOCUMENTO_FIELD = "DOCUMENTO"
NOMBRES_FIELD = "NOMBRES"
TIPO_VINCULACION_FIELD = "TIPO_VINCULACION"
TITULO_FIELD = "TITULO"
FECHA_NACIMIENTO_FIELD = "FECHA_NACIMIENTO"
EMAIL_FIELD = "EMAIL"

ESTUDIOS_KEY = "estudios"
PROFESOR_KEY = "profesor"


class Command(BaseCommand):
    args = 'professors.csv'
    help = 'Importa los docentes del archivo CSV en la base de datos.'

    def handle(self, *args, **options):

        # Verifica que se envíe un csv al script
        if len(args) != 1:
            raise CommandError("Debe agregar el archivo csv con información de docentes a agregar.")

        # Verfica que el archivo exista en el sistema
        csvPath = args[0]
        if not os.path.exists(csvPath):
            raise CommandError("%s no existe." % csvPath)

        # Inicia la lectura del csv y agrupa los profesores por número de documento, creando una lista de estudios.
        professors = dict()
        with open(csvPath, 'rb') as csvFile:
            reader = csv.DictReader(csvFile, delimiter=',', quotechar="\"")

            # Verificamos que el CSV tenga los campos que necesitamos
            required_fields = [CODIGO_FIELD, DOCUMENTO_FIELD, NOMBRES_FIELD, TIPO_VINCULACION_FIELD, TITULO_FIELD,
                               FECHA_NACIMIENTO_FIELD, EMAIL_FIELD]
            for row in reader:
                fields_name = row.keys()
                for i, _ in enumerate(fields_name):
                    fields_name[i] = fields_name[i].upper()
                    if not fields_name[i] in required_fields:
                        raise CommandError("El campo %s no existe en el archivo y es requerido." % (fields_name[i]))

                # Agregarmos al docente si no existe aún, si existe solo agregamos un titulo
                if row[DOCUMENTO_FIELD] in professors:
                    professors[DOCUMENTO_FIELD] = {PROFESOR_KEY: row, ESTUDIOS_KEY: []}
                professors[DOCUMENTO_FIELD][ESTUDIOS_KEY].append(row[TITULO_FIELD])

        # Iniciamos la insersión de docentes en la base de datos
        for professor_document in professors:
            professor = professors[professor_document][PROFESOR_KEY]
            print("Creando docente {} ...".format(professor[NOMBRES_FIELD]))
            nombres, apellidos = get_nombres_apellidos(professor[NOMBRES_FIELD])
            docente = Docente()
            docente.apellidos = apellidos
            docente.nombre = nombres
            docente.cedula = professor[DOCUMENTO_FIELD]
            docente.codigo = professor[CODIGO_FIELD]
            docente.email = professor[EMAIL_FIELD]

            # Se agregan los titulos del docente
            for titulo in professors[professor_document][TITULO_FIELD]:
                try:
                    docente_titulo = Titulo_Docente.objects.get(nombre=titulo)
                except Titulo_Docente.DoesNotExist:
                    docente_titulo = Titulo_Docente()
                    docente_titulo.nombre = titulo
                    docente_titulo.nivel_formacion = Titulo_Docente.nivel_formacion[0]
                    docente_titulo.save()
                docente.titulo.add(docente_titulo)
            docente.save()
            print("Docente {} creado correctamente.".format(professor[NOMBRES_FIELD]))


def get_nombres_apellidos(nombre):
    nombres_split = nombre.split(' ')
    apellidos = nombres_split[0] + " " + nombres_split[1]
    nombre = ""
    for x in range(2, len(nombres_split) - 1):
        nombre += nombres_split[x]
    return nombre, apellidos

