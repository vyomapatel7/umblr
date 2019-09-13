from django.forms import ModelForm
from .models import Blog, Post

class BlogCreateAndEditForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('blogTitle', 'blogBio', 'blogImage')

class PostCreateAndEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ('postTitle', 'postText', 'postImage')