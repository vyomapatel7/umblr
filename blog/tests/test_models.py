from django.test import TestCase

from blog.models import Blog

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(blogTitle='Test Title', blogBio='Test Bio')

    def test_blog_title_field(self):
        blog = Blog.objects.get(id=1)
        blog_title_field = blog._meta.get_field('blogTitle').verbose_name
        self.assertEquals(blog_title_field, 'blogTitle')

    def test_blog_Bio_field(self):
        blog = Blog.objects.get(id=1)
        blog_bio_field = blog._meta.get_field('blogBio').verbose_name
        self.assertEquals(blog_bio_field, 'blogBio')

    def test_blog_bio_field_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('blogTitle').max_length
        self.assertEquals(max_length, 200)

    # how do i test for an image field?
