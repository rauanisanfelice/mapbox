# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ENDERECOS(models.Model):
    LATITUDE = models.DecimalField(max_digits=30, decimal_places=10)
    LONGITUDE = models.DecimalField(max_digits=30, decimal_places=10)
    RAIO = models.IntegerField()
    ATIVO = models.BooleanField()

class LOJAS(models.Model):
    DESCRICAO = models.CharField(max_length=150)
    LATITUDE = models.DecimalField(max_digits=30, decimal_places=10)
    LONGITUDE = models.DecimalField(max_digits=30, decimal_places=10)
    RAIO = models.IntegerField()

class AREAS(models.Model):
    ID_AREA = models.IntegerField()
    DESCRICAO = models.CharField(max_length=150)
    LATITUDE = models.DecimalField(max_digits=30, decimal_places=10)
    LONGITUDE = models.DecimalField(max_digits=30, decimal_places=10)
    ORDEM = models.IntegerField()
    ATIVO = models.BooleanField()
