from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from forms import GameForm
from datetime import datetime
from models import Game
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

@login_required
def user_profile(request):
    user = request.user
    games = Game.objects.filter(user=user)
    context = {'games': games, 'user': user}

    return render_to_response('userprofile.html', context=context)

@login_required
def add_game(request):
    user = request.user
    error_message = None

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/userprofile')
        else:
            error_message = "Invalid Input"
    else:
        form = GameForm()

    args = {}
    args.update(csrf(request))
    args['user'] = user
    args['form'] = form
    args['error_message'] = error_message

    return render_to_response('addgame.html', args)

@login_required
def edit_game(request, id):
    user = request.user
    game = Game.objects.get(id=id)

    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form = form.save(commit=False)
            if game.deleteGame == True:
                instance = Game.objects.get(id=game.id)
                instance.delete()
                return HttpResponseRedirect('/userprofile')
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/userprofile')
    else:
        form = GameForm(instance=game)

    if request.POST.get('delete'):
        game.delete()
        return HttpResponseRedirect('/userprofile')

    args = {}
    args.update(csrf(request))
    args['user'] = user
    args['form'] = form
    args['game'] = game

    return render_to_response('editgame.html', args)