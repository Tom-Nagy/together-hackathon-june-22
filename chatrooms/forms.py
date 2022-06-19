from django import forms
from .models import Chatroom, Comment

class AddChatroomForm(forms.ModelForm):

    class Meta:
        model = Chatroom
        fields = ('subject', 'name',)


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Ask a Question',
        }

        self.fields['content'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
