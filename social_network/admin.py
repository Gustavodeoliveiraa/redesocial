from django.contrib import admin
from .models import ProfilePersonal
# Register your models here.


@admin.register(ProfilePersonal)
class adm(admin.ModelAdmin):
    pass