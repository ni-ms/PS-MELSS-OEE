from django.db import models

# Create your models here.
class OEEValues(models.Model):
    machineid = models.CharField(max_length=255)
    oeevalue = models.FloatField()
    Avalue = models.FloatField()
    Pvalue = models.FloatField()
    Qvalue = models.FloatField()
