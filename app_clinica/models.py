from django.db import models


class Medico(models.Model):
    nome = models.CharField(
        max_length=150,
        null=False,
        default='Nen'
    ),
    crm = models.CharField(
        max_length=5,
        primary_key=False,
        default='Null'
    ),
    espesializacao = models.CharField(
        max_length=50,
        default='especialização'
    )


class Paciente(models.Model):
    nome = models.CharField(
        max_length=150,
        null=False,
        default='N/A'
    ),
    cpf = models.CharField(
        max_length=14,
        primary_key=False,
        default='000.000.000-00'
    ),
    contato = models.CharField(
        max_length=14
    ),

    consulta = models.ManyToManyField(
        Medico
    )
