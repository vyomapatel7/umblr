from django.forms import ModelForm
from .models import Blog, Post

class BlogCreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('blogTitle', 'blogBio', 'blogImage')

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('postTitle', 'postText')