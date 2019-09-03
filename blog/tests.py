from django.test import TestCase
from django.urls import resolve
from blog.views import home
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)
