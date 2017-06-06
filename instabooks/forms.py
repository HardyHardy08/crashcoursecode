from django import forms
from .models import Album, Entry


class AlbumForm(forms.ModelForm):
    """Form for creating a new album"""
    class Meta:
        model = Album
        fields = ['text']
        labels = {'text': 'Album Name'}


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('text', 'image')
        labels = {'text': '', 'image': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
            'image': forms.FileInput()
        }
