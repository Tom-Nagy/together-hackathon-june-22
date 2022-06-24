'''Create and configure the profile form'''

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    ''' Configure the profile form '''
    class Meta:
        ''' Form meta properties '''
        model = UserProfile
        fields = ('username', 'email', 'about',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'username',
            'email': 'email address',
            'about': 'Tell us who you are...',
        }

        for field in self.fields:
            placeholder = f'{placeholders[field]}'
        self.fields[field].widget.attrs['placeholder'] = placeholder
