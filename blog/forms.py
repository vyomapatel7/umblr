from django.forms import ModelForm
from .models import Blog, Post
from django.utils.translation import gettext_lazy as _


class BlogCreateAndEditForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('blogTitle', 'blogBio', 'blogImage')
        labels = {
            'blogTitle': _('Title'),
            'blogBio': _('Bio'),
            'blogImage': _('Blog Image'),
        }


class PostCreateAndEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ('postTitle', 'postText', 'postImage')
        labels = {
            'postTitle': _('Title'),
            'postText': _('Text'),
            'postImage': _('Image'),
        }
