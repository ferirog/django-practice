from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, board_topics
from .models import Board

class HomeTests(TestCase):

    def setup(self):
        self.board = Board.objects.create(name='Django',description='Django board')
        url = reverse('home')
        self.response = self.client.get(url)

    #Testing the status code of the response is 200 (success)
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    #Test if Django returned the correct view function for the requested url
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    #Using assertcontains to test if the response body 
    #contains a given text
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))    

class BoardTopicTest(TestCase):
    #Prepare the environment to run the test, so to simulate a scenario
    def setup(self):
        Board.objects.create(name = 'Django', description = 'Django board')
    
    #Testing if Django is returning a status code 200 (success)
    #for an existing board.
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    #Testing if Django is returning a status code 404 (page not found)
    #for a board that doesn't exist in the database'
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    #Testing if Django is using the correct view function 
    #to render the topics
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEqual(view.func, board_topics)