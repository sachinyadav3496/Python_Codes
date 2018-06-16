from django.db import models

# Create your models here.

class user(models.Model):

    name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=50)

    contact_no = models.IntegerField()
    address = models.TextField()
    profile_pic = models.ImageField()



