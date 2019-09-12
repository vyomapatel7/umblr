from django.test import TestCase

from blog.models import Blog, Post

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(blogTitle='Test Title', blogBio='Test Bio')

    def test_blog_title_field(self):
        blog = Blog.objects.get(id=1)
        blog_title_field = blog._meta.get_field('blogTitle').verbose_name
        self.assertEquals(blog_title_field, 'blogTitle')

    def test_blog_bio_field(self):
        blog = Blog.objects.get(id=1)
        blog_bio_field = blog._meta.get_field('blogBio').verbose_name
        self.assertEquals(blog_bio_field, 'blogBio')

    def test_blog_title_field_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('blogTitle').max_length
        self.assertEquals(max_length, 200)

    def test_blog_bio_field_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('blogBio').max_length
        self.assertEquals(max_length, 500)

    # how do i test for an image field?

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(postTitle='testposttile', postText='testposttext')

    def test_post_title_field(self):
        post = Post.objects.get(id=1)
        post_title_field = post._meta.get_field('postTitle').verbose_name
        self.assertEquals(post_title_field, 'postTitle')
