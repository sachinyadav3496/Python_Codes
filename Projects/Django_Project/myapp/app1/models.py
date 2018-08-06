from django.db import models

# Create your models here.
class mydata(models.Model):

    name = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100,default=None)
    email = models.EmailField(default=None)
