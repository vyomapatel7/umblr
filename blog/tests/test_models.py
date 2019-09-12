from django.test import TestCase

from blog.models import Blog

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(blogTitle='Test Title', blogBio='Test Bio')

    def test_blog_title(self):
        blog = Blog.objects.get(id=1)
        blog_title_field = blog._meta.get_field('blogTitle').verbose_name
        self.assertEquals(blog_title_field, 'blogTitle')
