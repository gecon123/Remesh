from django.test import TestCase
from myapp.models import Conversation, Message, Thought

class TestModels(TestCase):

    def test_conversation(self):
        convo = Conversation.objects.create(
            title='Conversation 1',
            start_date=date(2020, 9, 20)
        )

        self.assertEquals(self.convo.title, 'Conversation 1')
        self.assertEquals(self.convo.start_date, date(2020, 9, 20))
    
    def test_message(self):
        mess = Message.objects.create(
            title='Message 1',
            start_time=datetime(2020, 9, 20, 11, 00, 00, 00, 000000)
        )

        self.assertEquals(self.mess.title, 'Message 1')
        self.assertEquals(self.mess.start_time, datetime(2020, 9, 20, 11, 00, 00, 00, 000000))

    def test_message(self):
        tho = Thought.objects.create(
            title='Thought 1',
            start_time=datetime(2020, 9, 20, 11, 00, 00, 00, 000000)
        )

        self.assertEquals(self.tho.title, 'Thought 1')
        self.assertEquals(self.tho.start_time, datetime(2020, 9, 20, 11, 00, 00, 00, 000000))