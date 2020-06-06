from django.db import models

# Create your models here.

class Plans(models.Model):
    pname =models.CharField(max_length=20)
    pp_start_time = models.DateField()
    pp_long = models.IntegerField()
    pstart_time = models.DateField()
    pover_time = models.DateField()
    plong = models.IntegerField()
    pscore = models.IntegerField()
    pstudent = models.ForeignKey("Students",on_delete=models.CASCADE)

class Students(models.Model):
    sname =models.CharField(max_length=20)
    sgrage = models.CharField(max_length=20)
    sclass =models.CharField(max_length=20)
    sage = models.IntegerField()
