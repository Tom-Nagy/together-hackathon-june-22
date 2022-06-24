'''Create and configure the chatroom and comment form'''

from django import forms
from .models import Chatroom, Comment


class AddChatroomForm(forms.ModelForm):
    ''' Configure the chatroom form '''
    class Meta:
        ''' Form meta properties '''
        model = Chatroom
        fields = ('name', 'subject',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Give a name to this chatroom',
            'subject': 'Start the discussion with a question or a statement',
        }

        for field in self.fields:
            placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Participate in the discussion',
        }

        self.fields['content'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
