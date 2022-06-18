from django.shortcuts import render
from .models import Chatroom
from .forms import AddChatroomForm

# Create your views here.

def chatrooms(request):
    """
    A view to display all the chatrooms and add a
    new chatroom.
    """
    chatrooms = Chatroom.objects.all()
    add_chatroom_form = AddChatroomForm()

    if request.method == "POST":
        form_data ={
            'subject' : request.POST['subject'],
            'name' : request.POST['name'],
        }

        chatroom_form = AddChatroomForm(form_data)
        if chatroom_form.is_valid():
            chatroom_form.save()


    template = 'chatrooms/chatrooms.html'
    context = {
        'chatrooms': chatrooms,
        'add_chatroom_form' :add_chatroom_form,
    }

    return render(request, template, context)
