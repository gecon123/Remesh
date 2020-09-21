from django.db import models
from django.urls import reverse

# Create your models here.
class Conversation(models.Model):
    title = models.TextField()
    start_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

class Message(models.Model):
    convo = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    title = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

class Thought(models.Model):
    mess = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='thoughts')
    title = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')
