from django.urls import reverse, resolve
from django.test import TestCase
from .views import home

class HomeTests(TestCase):
    #Testing the status code of the response is 200 (success)
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    #Test if Django returned the correct view function for the requested url
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)