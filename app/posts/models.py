from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    """Model class for posts"""
    title = models.CharField(max_length=255)
    url = models.URLField()
    poster = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Vote(models.Model):
    """Model class for votes"""
    voter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
