from django import forms
from .models import Chatroom, Comment

class AddChatroomForm(forms.ModelForm):

    class Meta:
        model = Chatroom
        fields = ('subject', 'name',)


