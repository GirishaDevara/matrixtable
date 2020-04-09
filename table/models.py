from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=255)
    cost = models.FloatField()
    image_url = models.CharField(max_length=2083)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name


class employee(models.Model):
    ename = models.CharField(max_length=255)
    eid = models.IntegerField()
    email=models.EmailField(max_length=254)
    def __str__(self):
        return self.ename

