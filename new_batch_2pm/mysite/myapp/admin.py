from django.contrib import admin
from .models import bank
# Register your models here.
admin.site.register(bank)
#create admin user running create super user command
#python manage.py shell to run a shell for the project