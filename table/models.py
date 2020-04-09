from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    image_url = models.CharField(max_length=2083)
    description = models.CharField(max_length=1000)

