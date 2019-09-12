from django.test import TestCase

from blog.models import Blog

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(blogTitle='Test Title', blogBio='Test Bio')

    def test_blog_title_field(self):
        blog = Blog.objects.get(id=1)
        blog_Title_field = blog._meta.get_field('blogTitle').verbose_name
        self.assertEquals(blog_Title_field, 'blogTitle')

    def test_blog_Bio_field(self):
        blog = Blog.objects.get(id=1)
        blog_Bio_field = blog._meta.get_field('blogBio').verbose_name
        self.assertEquals(blog_Bio_field, 'blogBio')
