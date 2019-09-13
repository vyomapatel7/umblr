from django.test import TestCase

from blog.forms import BlogCreateAndEditForm, PostCreateAndEditForm

class BlogCreateAndEditTest(TestCase):
    def test_blog_create_and_edit_form_title_field_label(self):
        form = BlogCreateAndEditForm()
        self.assertTrue(form.fields['blogTitle'].label == 'BlogTitle')

    def test_blog_create_and_edit_form_bio_field_label(self):
        form = BlogCreateAndEditForm()
        self.assertTrue(form.fields['blogBio'].label == 'BlogBio')

    def test_blog_create_and_edit_form_image_field_label(self):
        form = BlogCreateAndEditForm()
        self.assertTrue(form.fields['blogImage'].label == 'BlogImage')

    # How to test image part of form?


class PostCreateAndEditTest(TestCase):
    def test_post_create_and_edit_form_title_field_label(self):
        form = PostCreateAndEditForm()
        self.assertTrue(form.fields['postTitle'].label == 'PostTitle')

    def test_post_create_and_edit_form_text_field_label(self):
        form = PostCreateAndEditForm()
        self.assertTrue(form.fields['postText'].label == 'PostText')

    def test_post_create_and_edit_form_image_field_label(self):
        form = PostCreateAndEditForm()
        self.assertTrue(form.fields['postImage'].label == 'PostImage')
