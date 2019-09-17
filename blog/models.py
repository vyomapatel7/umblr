from django.db import models
from django.conf import settings
from django.urls import reverse


class Blog(models.Model):
    blogTitle = models.CharField(max_length=200, blank=False)
    blogBio = models.CharField(max_length=500, blank=True)
    blogImage = models.ImageField(default='default.jpg', upload_to='blogImages')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.blogTitle}"


class Post(models.Model):
    postTitle = models.CharField(max_length=200, blank=False)
    postText = models.CharField(max_length=1000, blank=True)
    postImage = models.ImageField(default='default.jpg', upload_to='blogImages')
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.postTitle}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Connection(models.Model):
    beingFollowed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="beingFollowed")
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return self.beingFollowed.blog.blogTitle
