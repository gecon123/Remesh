from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import FirstView, MessView, ThoView, AddConvoView, AddMessView, AddThoView, searchbar

class TestUrls(SimpleTestCase):

    def test_conversation_url(self):
        url = reverse('home')
        self.assertEquals(resolved(url).func, FirstView)

    def test_message_url(self):
        url = reverse('conversations_by_id')
        self.assertEquals(resolved(url).func, MessView)

    def test_thought_url(self):
        url = reverse('messages_by_id')
        self.assertEquals(resolved(url).func, ThoView)

    def test_add_convo_url(self):
        url = reverse('add_convo')
        self.assertEquals(resolved(url).func, AddConvoView)

    def test_add_mess_url(self):
        url = reverse('add_mess')
        self.assertEquals(resolved(url).func, AddMessView)
    
    def test_add_tho_url(self):
        url = reverse('add_tho')
        self.assertEquals(resolved(url).func, AddThoView)

    def test_searchbar_url(self):
        url = reverse('searchbar')
        self.assertEquals(resolved(url).func, searchbar)
    