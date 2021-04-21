from django.contrib import admin

from .models import Blogs, Comment


class BlogsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "description", "time", "active"]
    list_editable = ["active"]
    class meta:
        model = Blogs


class CommentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "date", "email"]

    class meta:
        model = Comment


admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Comment, CommentAdmin)
