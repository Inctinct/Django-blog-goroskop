from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','text')
    list_filter = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'author')
    list_filter = ('author',)


admin.site.register(Post, PostAdmin)


admin.site.register(Comment, CommentAdmin)