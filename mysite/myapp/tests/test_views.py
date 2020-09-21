from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Conversation, Message, Thought
import json

class TestViews(TestCase):

    def test_first_view(self):
        client = Client()
        response = client.get(reverse('conversations'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversation_details.html')

    def test_mess_view(self):
        client = Client()
        response = client.get(reverse('messages'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'message_details.html')

    def test_tho_view(self):
        client = Client()
        response = client.get(reverse('thoughts'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'thought_details.html')

    def test_add_convo_view(self):
        client = Client()
        response = client.get(reverse('conversation'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_convo.html')

    def test_add_mess_view(self):
        client = Client()
        response = client.get(reverse('message'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_mess.html')

    def test_add_tho_view(self):
        client = Client()
        response = client.get(reverse('thought'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_tho.html')

    def test_searchbar(self):
        client = Client()
        response = client.get(reverse('search'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'searchbar.html')