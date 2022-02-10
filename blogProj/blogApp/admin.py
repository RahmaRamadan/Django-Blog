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











# class StudentAdmin(admin.ModelAdmin):
#     fieldsets=(
#     ["student Information",{'fields':["fname","lname","age"]}],
#     ["Scholarship Information",{'fields':["student_track"]}]
#     )
#     list_display=("fname","lname","age","student_track","is_graduate")
#     list_filter=["fname","age","student_track"]
#     search_fields=["fname","age","student_track__track_name"]
# class InlineStudent(admin.StackedInline):
#     model=Student
#     extra =2
# class TrackAdmin(admin.ModelAdmin):
#     inlines=[InlineStudent]

    
# admin.site.register(Student,StudentAdmin)
# admin.site.register(Track,TrackAdmin)

