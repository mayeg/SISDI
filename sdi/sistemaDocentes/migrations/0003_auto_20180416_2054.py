# Generated by Django 2.0.3 on 2018-04-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaDocentes', '0002_auto_20180416_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficios',
            name='plazo_entrega',
            field=models.IntegerField(),
        ),
    ]
