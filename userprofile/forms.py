from django import forms
from models import Game
from django.contrib.auth.models import User

class GameForm(forms.ModelForm):

    image = forms.ImageField(required=False)

    class Meta:
        model = Game
        fields = ('user','title','image','description','requirements','code')

User.game = property(lambda u: Game.objects.get_or_create(user=u)[0])