from django.contrib import admin
from .models import ProfilePersonal, Status, Friends, Post, Notifications
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


@admin.register(Post)
class post(admin.ModelAdmin):
    pass


@admin.register(Notifications)
class notification(admin.ModelAdmin):
    pass
