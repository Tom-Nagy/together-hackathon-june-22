from codecs import charmap_build
from django.shortcuts import render
from .models import Chatroom, Comment

# Create your views here.

def chatrooms(request):
    """
    A view to display all the chatrooms
    """
    chatrooms = Chatroom.objects.all()


    template = 'chatrooms/chatrooms.html'
    context = {
        'chatrooms': chatrooms,
    }



    return render(request, template, context)
