from django import forms
from models import Game
from django.contrib.auth.models import User
from pagedown.widgets import PagedownWidget

class GameForm(forms.ModelForm):

    image = forms.ImageField(required=False)
    code = forms.CharField(widget=PagedownWidget())
    #user = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    deleteGame = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Game.objects.all())

    class Meta:
        model = Game
        fields = ('title','image','description','requirements','code', 'deleteGame')

#User.game = property(lambda u: Game.objects.get_or_create(user=u)[0])