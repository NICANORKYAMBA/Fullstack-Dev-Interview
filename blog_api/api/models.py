""" Models. """
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BlogPost(models.Model):
    """
    A blog post.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
