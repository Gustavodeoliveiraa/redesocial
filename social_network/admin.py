from django.contrib import admin
from .models import ProfilePersonal, Status, Friends
# Register your models here.


@admin.register(ProfilePersonal)
class adm(admin.ModelAdmin):
    pass


@admin.register(Status)
class status(admin.ModelAdmin):
    pass


@admin.register(Friends)
class friends(admin.ModelAdmin):
    pass

