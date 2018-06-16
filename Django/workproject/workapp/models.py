from django.db import models

# Create your models here.
class UserProfile(models.Model):

    name = models.CharField(max_length=50,verbose_name="Name")
    login = models.CharField(max_length=25,verbose_name="Login")
    password = models.CharField(max_length=100,verbose_name='Password')
    phone = models.CharField(max_length=20,verbose_name="Phone number",null=True,default=None,blank=True)
    born_date = models.DateField(verbose_name="Born date",null=True,default=None,blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection",null=True,default=None,blank=True)
    email = models.EmailField(verbose_name="Email")
    years_seniority = models.IntegerField(verbose_name="Seniority",default=0)
    date_created = models.DateField(verbose_name="Date of Birthday",auto_now_add=True)

    def __str__(self):

        return self.name

class Project(models.Model):

    title = models.CharField(max_length=50,verbose_name="Title")
    description = models.CharField(max_length=1000,verbose_name="Description")
    client_name = models.CharField(max_length=1000,verbose_name="Client name")

    def __str__(self):

        return self.title

class Task(models.Model):

    title = models.CharField(max_length=50,verbose_name="Title")
    description = models.CharField(max_length=1000,verbose_name='Description')
    time_elapsed = models.IntegerField(verbose_name="Elapsed time",null=True,default=None,blank=True)
    importance = models.IntegerField(verbose_name="Imoprtance")
    project = models.ForeignKey(Project,verbose_name="Project",null=True,default=None,blank=True)
    app_user = models.ForeignKey(UserProfile,verbose_name="User")

    def __str__(self):
        return self.title


"""
class Supervisor(UserProfile):
# Duplicated common fields
    specialisation = models.CharField(max_length=50, verbose_name="Specialisation")
class Developer(UserProfile):
# Duplicated common fields
    supervisor = models.ForeignKey(Supervisor, verbose_name="Supervisor")
    """
