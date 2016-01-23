from django.shortcuts import render_to_response
from django.http import HttpResponse
from userprofile.models import Game

def index(request):
    return render_to_response('base.html', )

def home_page(request):
    user = request.user
    username = user.username
    games = Game.objects.order_by('-pk')[:3]
    context = {'games': games, 'user': user, 'username': username}

    return render_to_response('homepage.html', context=context)