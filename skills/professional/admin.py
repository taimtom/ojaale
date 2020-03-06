from django.contrib import admin

# Register your models here.
from .models import Professional, Testimony

admin.site.register(Professional)

admin.site.register(Testimony)