from rest_framework import serializers
from .models import Post, Comment, Vote, Follow
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
      model = Post
      fields = ('id', 'created', 'modified', 'author', 'body','comments', 'follows')

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
      model = Comment
      fields = ('id', 'created', 'modified', 'body', 'commenter', 'post')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('id', 'username', 'first_name', 'last_name', 'email')

class VoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vote
    fields = ('id', 'username', 'first_name', 'last_name', 'email')

    list_display = ('id', 'created', 'modified', 'voter', 'post', 'liked')
    list_filter = ('created', 'modified', 'voter', 'post', 'liked')

class FollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Follow
    fields = ('id', 'created', 'modified', 'follower', 'post')