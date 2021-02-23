from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.IntegerField()
    office = models.CharField(max_length=100)
    workload = models.IntegerField()
    admission_date = models.DateField()
