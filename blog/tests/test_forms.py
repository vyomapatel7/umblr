from django.test import TestCase

from blog.forms import BlogCreateForm

class BlogCreateTest(TestCase):
    def test_blog_create_form_title_field_label(self):
        form = BlogCreateForm()
        self.assertTrue(form.fields['blogTitle'].label == 'BlogTitle')

    def test_blog_create_form_text_field_label(self):
        form = BlogCreateForm()
        self.assertTrue(form.fields['blogBio'].label == 'BlogBio')
