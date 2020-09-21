from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView # all conversations v one
from .models import Conversation, Message, Thought
from django import forms

def index(request):
    return HttpResponse("Please navigate to the conversations page to get started!")

class FirstView(ListView):
    model = Conversation
    template_name = 'conversation_details.html'

class MessView(ListView):
    model = Message
    template_name = 'message_details.html'

class ThoView(ListView):
    model = Thought
    template_name = 'thought_details.html'

class AddConvoView(CreateView):
    model = Conversation
    template_name = 'add_convo.html'
    fields = '__all__'

class AddMessView(CreateView):
    model = Message
    template_name = 'add_mess.html'
    fields = '__all__'

class AddThoView(CreateView):
    model = Thought
    template_name = 'add_tho.html'
    fields = '__all__'

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        convos = Conversation.objects.all().filter(title=search)
        return render(request, 'searchbar.html', {'convos': convos})