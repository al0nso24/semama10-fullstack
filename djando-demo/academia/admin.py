#academia/admin.py
from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
 list_display = ('nombre', 'dni', 'edad')
 search_fields = ('nombre', 'dni')