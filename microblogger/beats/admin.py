from django.contrib import admin

from .models import Post, Vote, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'author', 'body')
    list_filter = ('created', 'modified', 'author')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'voter', 'post', 'liked')
    list_filter = ('created', 'modified', 'voter', 'post', 'liked')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'body', 'commenter', 'post')
    list_filter = ('created', 'modified', 'commenter', 'post')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'follower', 'post')
    list_filter = ('created', 'modified', 'follower', 'post')