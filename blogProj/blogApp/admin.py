from dataclasses import field
from django.contrib import admin
from .models import User,Category,Post,Comment,Tag
# # Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ["User Info", {'fields':["username","email","password"]}],
    )
    list_display=("username","email","password")
    list_filter=["username","email"]
    search_fields=["username","password"]

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ["category info", {'fields':["name","followers"]}],
    )
    # list_display=("name","followers")
    search_fields=["name"]

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ["post info", {'fields':["title","postpicture","content","category","tags","user"]}],
    )
    # list_display=("title","postpicture","content","category","tags","user","date")
    search_fields=["user"]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ["comment info", {'fields':["body","post","user","date_added"]}],
    )
    list_display=("body","post","user")
    search_fields=["post","user"]


class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        ["tag info", {'fields':["name"]}],
    )
   


admin.site.register(User,UserAdmin)
admin.site.register( Category,CategoryAdmin)
admin.site.register( Post,PostAdmin)
admin.site.register( Comment,CommentAdmin)
admin.site.register( Tag,TagAdmin)














