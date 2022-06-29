from django.db import models

# Create your models here.

class Cloth(models.Model):
    head= models.CharField(max_length=250)
    description = models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.head