from django.db import models

# Create your models here.

class Address(models.Model):
    hno = models.CharField(max_length=10)
    street_addr = models.CharField(max_length=60)
    city  = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    def __str__(self):
        addr = self.hno+','+self.street_addr+','+self.city\
        +','+self.state+', '+self.country
        return addr
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    ph_no = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Faculty(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=50)
    ph_no = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    fees = models.FloatField(max_length=6)
    due = models.FloatField(max_length=6)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    def __str__(self):
        return self.course
