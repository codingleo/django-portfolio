from django.contrib import admin

# Register your models here.
from .models import Job

class JobsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobsAdmin)