from dataclasses import field
from django.contrib import admin
from .models import User,Category,Post,Comment,Tag, UsersCategories



class UserCategoryInline(admin.TabularInline):
    model = UsersCategories
    extra = 1


# class UserAdmin(admin.ModelAdmin):

#     list_display = ("id", "username", "email", "password")
#     list_filter = ["username", "email"]
#     search_fields = ["username"]
#     inlines = (UserCategoryInline,)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'show_followers')
    list_filter = ["name"]
    search_fields = ["name"]
    inlines = (UserCategoryInline,)

# class PostAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ["post info", {'fields':["title","postpicture","content","category","tags","user"]}],
#     )
#     def get_tags(self,obj):
#         return "\n".join([p.name for p in obj.tags.all()])

# class PostAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ["post info", {'fields': ["title", "postpicture",
#                                   "content", "category", "tags", "user"]}],
#     )
#     def get_tags(self,obj):
#         return "\n".join([p.name for p in obj.tags.all()])

#     list_display=("title","postpicture","content","category","get_tags","user")
#     search_fields=["user"]

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ["comment info", {'fields':["body","post","user"]}],
    )
    list_display=("body","post","user")
    search_fields=["post","user"]


class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        ["tag info", {'fields':["name"]}],
    )
   




# admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
