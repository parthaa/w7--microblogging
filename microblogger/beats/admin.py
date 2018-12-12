from django.contrib import admin
from beats.models import Post, Comment, Vote, Follow


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ( 'author', 'body')


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('body', 'commenter')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote)
admin.site.register(Follow)