from django.db import models

# Create your models here.
class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    plant_type = models.CharField(max_length=255)
    plant_number = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
