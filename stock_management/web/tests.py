from django.core.urlresolvers import resolve
from django.test import TestCase

from web.views import home_page
from django.http.request import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertEquals(response.content[0:6], '<html>')
        self.assertIn('<title>Home</title>', response.content)
        self.assertEquals(response.content[-7:], '</html>')
