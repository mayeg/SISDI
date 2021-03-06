# Generated by Django 2.0.3 on 2018-06-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaDocentes', '0009_remove_departamento_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulo_docente',
            name='nivel_formacion',
            field=models.CharField(choices=[('tecnologia', 'Tecnologia'), (' pregrado ', ' Pregrado '), (' especializacion ', ' Especializacion '), (' maestria ', ' Maestria '), (' doctorado ', ' Doctorado '), ('phd', 'PhD')], default='No seleccion', max_length=50),
        ),
        migrations.AlterField(
            model_name='titulo_docente',
            name='nombre',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
