from django.contrib import admin
from .models import ProfilePersonal, Status
# Register your models here.


@admin.register(ProfilePersonal)
class adm(admin.ModelAdmin):
    pass

@admin.register(Status)
class status(admin.ModelAdmin):
    pass