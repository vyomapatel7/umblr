from django.db import models
from django.conf import settings

class Blog(models.Model):
    blogTitle = models.CharField(max_length=200, blank=False)
    blogBio = models.CharField(max_length=500, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )

class Post(models.Model):
    postTitle = models.CharField(max_length=200, blank=False)
    postText = models.CharField(max_length=1000, blank=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, blank=True, null=True
    )
