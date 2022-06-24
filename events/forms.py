'''Create and configure the chatroom and comment form'''

from django import forms
from .models import Event


class DateField(forms.ModelForm):
    """
    A class to create date picker
    """
    date = forms.DateField(
    widget=forms.TextInput(
        attrs={'type': 'date'}
    )
)


class AddEventForm(DateField):
    ''' Configure the Event form'''
    class Meta:
        ''' Form meta properties '''
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'event_name': 'Event name',
            'date': 'Date of the event',
            'location': 'Location of the event',
            'description': 'Add a description',
            'image': 'Add a image for this event',
        }

        self.fields['event_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
