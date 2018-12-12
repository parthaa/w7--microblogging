from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator
from model_utils.models import TimeStampedModel

class Post(TimeStampedModel):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
  body = models.TextField(null=True, blank=True, max_length=280, validators=[MinLengthValidator(2)])

  @staticmethod
  def find_with_comments(num_of_comments = 1):
    return Post.objects.annotate(comment_count = models.Count('comments')).filter(comment_count=num_of_comments)

class Vote(TimeStampedModel):
  voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="votes")
  liked = models.BooleanField(default=False)

  class Meta:
    unique_together= (('post', 'voter'),)

class Comment(TimeStampedModel):
  body = models.TextField(null=True, blank=True)
  commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="comments")

class Follow(TimeStampedModel):
  follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follows")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="follows")
