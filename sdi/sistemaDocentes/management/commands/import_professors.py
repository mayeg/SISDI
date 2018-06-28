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
EMAIL_FIELD = "EMAILI"

ESTUDIOS_KEY = "estudios"
PROFESOR_KEY = "profesor"


class Command(BaseCommand):
    args = 'professors'
    help = 'Importa los docentes del archivo CSV en la base de datos.'

    def add_arguments(self, parser):
        parser.add_argument('csv', nargs='+', type=str)

    def handle(self, *args, **options):
        # Verifica que se envíe un csv al script
        if len(options['csv']) != 1:
            raise CommandError("Debe agregar el archivo csv con información de docentes a agregar.")

        # Verfica que el archivo exista en el sistema
        csvPath = options['csv'][0]
        if not os.path.exists(csvPath):
            raise CommandError("El la archivo %s no existe." % csvPath)

        # Inicia la lectura del csv y agrupa los profesores por número de documento, creando una lista de estudios.
        professors = dict()
        print("Iniciando lectura del archivo ...")
        with open(csvPath) as csvFile:
            reader = csv.DictReader(csvFile, delimiter=',', quotechar="\"")

            # Verificamos que el CSV tenga los campos que necesitamos
            required_fields = [CODIGO_FIELD, DOCUMENTO_FIELD, NOMBRES_FIELD, TIPO_VINCULACION_FIELD, TITULO_FIELD,
                               FECHA_NACIMIENTO_FIELD, EMAIL_FIELD]
            for row in reader:
                fields_names = row.keys()
                for required_field in required_fields:
                    if required_field not in fields_names:
                        raise CommandError("El campo %s no existe en el archivo y es requerido." % required_field)

                # Agregarmos al docente si no existe aún, si existe solo agregamos un titulo
                if row[DOCUMENTO_FIELD] not in professors:
                    professors[row[DOCUMENTO_FIELD]] = {PROFESOR_KEY: row, ESTUDIOS_KEY: []}
                professors[row[DOCUMENTO_FIELD]][ESTUDIOS_KEY].append(row[TITULO_FIELD])

        print("Archivo leido correctamente")
        # Iniciamos la insersión de docentes en la base de datos
        for professor_document in professors:
            try:
                professor = professors[professor_document][PROFESOR_KEY]
                print("Creando docente {} ...".format(professor[NOMBRES_FIELD]))
                nombres, apellidos = get_nombres_apellidos(professor[NOMBRES_FIELD])
                docente = Docente()
                docente.apellidos = apellidos
                docente.nombre = nombres
                docente.cedula = professor[DOCUMENTO_FIELD]
                docente.codigo = professor[CODIGO_FIELD]
                docente.email = professor[EMAIL_FIELD]
                docente.save()
                # Se agregan los titulos del docente
                for titulo in professors[professor_document][ESTUDIOS_KEY]:
                    try:
                        docente_titulo = Titulo_Docente.objects.get(nombre=titulo)
                    except Exception as e:
                        docente_titulo = Titulo_Docente()
                        docente_titulo.nombre = titulo
                        docente_titulo.nivel_formacion = Titulo_Docente.NIVEL_FORMACION_CHOICES[0][0]
                        docente_titulo.save()
                    docente.titulo.add(docente_titulo)
                docente.save()
                print("Docente {} creado correctamente.".format(professor[NOMBRES_FIELD]))
            except Exception as e:
                print("Error guardando el docente {}.".format(professor[NOMBRES_FIELD]))


def get_nombres_apellidos(nombre):
    nombres_split = nombre.split(' ')
    apellidos = nombres_split[0] + " " + nombres_split[1]
    nombre = ""
    for x in range(2, len(nombres_split) - 1):
        nombre += nombres_split[x]
    return nombre, apellidos

