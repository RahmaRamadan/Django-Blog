from dataclasses import field
from django.contrib import admin
from .models import User
# # Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ["User Info", {'fields':["username","email","password"]}],
    )
    list_display=("username","email","password")
    list_filter=["username","email"]
    search_fields=["username","password"]
admin.site.register(User,UserAdmin)

