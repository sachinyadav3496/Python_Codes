p
from django.contrib import admin

# Register your models here.
from .models import UserProfile, Project, Task

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
