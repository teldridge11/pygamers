from django import forms
from models import Game

class GameForm(forms.ModelForm):

    image = forms.ImageField()
    code = forms.Textarea()
    deleteGame = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Game
        fields = ('title', 'image', 'description', 'requirements', 'code', 'deleteGame')