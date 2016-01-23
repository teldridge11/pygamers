from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from userprofile.models import Game

def games_view(request):
    user = request.user
    games = Game.objects.order_by('-pk')
    context = {'games': games, 'user': user}

    return render_to_response('games.html', context=context)