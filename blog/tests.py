from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import resolve
from blog.views import home, about, blog
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import Blog


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)


class AboutPageTest(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_resolves_to_about_page_view(self):
        found = resolve('/about/')
        self.assertEqual(found.func, about)

    def test_about_page_returns_correct_html(self):
        request = HttpRequest()
        response = about(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('about.html')
        self.assertEqual(html, expected_html)


# class LoginPageTest(TestCase): ???

class SignUpPageTest(TestCase):

    # does sign up page exist
    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    # foes it bring correct view
    # does it bring correct html
    # does password fiel dissallow less than 8 words?
    # does password field disallow only numbers?

class BlogPageTest(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(username="testuser")
        user.set_password('12345')
        user.save()
        blog = Blog.objects.create(blogTitle="Test", blogBio="Testbio", user=user)

    def test_blog_saved(self):
        blog = Blog.objects.get(id=1)
        expected_blog_name = f"{blog.blogTitle}"
        self.assertEqual(expected_blog_name, "Test")

    def test_blog_page_returns_correct_html(self):
        # b = Blog.objects.create(blogTitle="Test")
        request = HttpRequest()
        response = blog(request, id=1)
        html = response.content.decode('utf8')
        expected_html = render_to_string('blog.html', context={'blog': blog, 'request': request})
        self.assertEqual(html, expected_html)


# class EditBlogPageTest(self):

    # does  page exist
    # does it bring correct view
    # does it bring correct html
    # does submit redirect to correct page
    # does it contain correct content check for Blog new title?


# class PostPageTest(self):

    # does  page exist
    # does it bring correct view
    # does it bring correct html
    # does it contain correct content post title


# class EditPostPageTest(self):

    # does  page exist
    # does it bring correct view
    # does it bring correct html
    # does submit redirect to correct page
    # does it contain correct content check for post title?
