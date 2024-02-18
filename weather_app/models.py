from django.db import models

# Create your models here.

class city(models.Model):
    name = models.CharField(max_length=25,default='')

        # this function used to change object into string because the city name received object so 

    def __str__(self):
        return self.name