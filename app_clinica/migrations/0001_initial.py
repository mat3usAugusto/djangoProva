# Generated by Django 4.2.2 on 2023-06-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especializacao', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contato', models.CharField(max_length=60)),
                ('consulta', models.ManyToManyField(to='app_clinica.medico')),
            ],
        ),
    ]
