from django.db import models

# Create your models here.
class bank(models.Model): #don't forget to register in admin

    name = models.CharField(max_length=50)
    acc_no = models.IntegerField(primary_key=True)
    bal = models.IntegerField()
    password = models.CharField(max_length=20)
    image = models.ImageField()
