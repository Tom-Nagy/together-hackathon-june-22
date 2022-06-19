from django.shortcuts import (
    get_object_or_404, redirect, render, reverse)
from .models import Chatroom, Comment
from .forms import AddChatroomForm, AddCommentForm
from django.contrib import messages




def chatrooms(request):
    """
    A view to display all the chatrooms and add a
    new chatroom.
    """
    chatrooms = Chatroom.objects.all()
    add_chatroom_form = AddChatroomForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            form_data ={
                'subject' : request.POST['subject'],
                'name' : request.POST['name'],
            }

            chatroom_form = AddChatroomForm(form_data)
            if chatroom_form.is_valid():
                chatroom_form.save()
        else:
            messages.error(request, 'Please login or register to open a new chatroom!')



    template = 'chatrooms/chatrooms.html'
    context = {
        'chatrooms': chatrooms,
        'add_chatroom_form' :add_chatroom_form,
    }

    return render(request, template, context)


def chatroom_detail(request, chatroom_id):
    """
    A view to present the chatroms' content and hold the
    comment forms
    """

    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)

    if request.method == "POST":
        if request.user.is_authenticated:
            content = request.POST.get('content')

            Comment.objects.create(
                chatroom = chatroom,
                user = request.user,
                content = content,
                )
            return redirect('chatroom_detail', chatroom_id)
        else:
            messages.error(request, 'Please login or register to ask a question!')


    add_comment_form = AddCommentForm()
    template = 'chatrooms/chatroom_detail.html'
    context = {
        'chatroom' : chatroom,
            'add_comment_form' :add_comment_form,
        }

    return render(request, template, context)
