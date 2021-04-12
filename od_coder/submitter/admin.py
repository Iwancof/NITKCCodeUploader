from django.contrib import admin

# Register your models here.

from .models import Task, Submit

admin.site.register(Task)
admin.site.register(Submit)
