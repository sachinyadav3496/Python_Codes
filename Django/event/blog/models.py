from django.db import models

# Create your models here.
class event_blog(models.Model):

    title = models.CharField(max_length=50,null=False)
    time = models.DateTimeField(auto_created=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(null=True)

    def __self__(self):

        return self.title

class gallary(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(null=True)
    time = models.DateTimeField(auto_created=True)


    def __self__(self):

        return self.name
