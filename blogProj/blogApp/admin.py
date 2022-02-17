from dataclasses import field
from django.contrib import admin
from .models import User,Category,Post,Comment,Tag, UsersCategories, PostTags ,CommentReply



class UserCategoryInline(admin.TabularInline):
    model = UsersCategories
    extra = 1


class PostTagsInLine(admin.TabularInline):
    model = PostTags
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

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ["post info", {'fields': ["title", "postpicture", "content", "category", "user"]}],
    )
    def get_tags(self,obj):
        return "\n".join([p.name for p in obj.tags.all()])

    list_display=("title","postpicture","content","category","show_tags","user")
    search_fields=["user"]
    inlines = (PostTagsInLine,)

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ["comment info", {'fields':["body","post","user"]}],
    )
    def get_replies(self,obj):
        return "\n".join([p.body for p in obj.replies.all()])
    list_display=("body","post","user","get_replies")
    search_fields=["post","user"]


class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        ["tag info", {'fields':["name"]}],
    )
    list_display=("name",)
    inlines = (PostTagsInLine,)

class CommentReplyAdmin(admin.ModelAdmin) :
    fieldsets = (
        ["comment info", {'fields':["body","comment","user"]}],
    )
    list_display=("body","comment","user")
    search_fields=["comment","user"]





# admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
admin.site.register(Tag, TagAdmin)
