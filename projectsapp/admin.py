from django.contrib import admin
from . models import Project,Contactus,Feedback
# Register your models here.

admin.site.register((Project,Contactus,Feedback))