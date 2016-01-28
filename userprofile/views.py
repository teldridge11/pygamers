from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from forms import GameForm
from models import Game
from PIL import Image
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
#highlight(code, PythonLexer(), HtmlFormatter())

@login_required
def user_profile(request):
    user = request.user
    games = Game.objects.filter(user=user)
    context = {'games': games, 'user': user}

    return render_to_response('userprofile.html', context=context)

@login_required
def add_game(request):
    user = request.user

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            image = Image.open(form.image)
            box = (0, 0, 200, 200)
            cropped = image.crop(box)
            #form.image = cropped
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/userprofile')
    else:
        form = GameForm()

    args = {}
    args.update(csrf(request))
    args['user'] = user
    args['form'] = form

    return render_to_response('addgame.html', args)

@login_required
def edit_game(request, id):
    user = request.user
    game = Game.objects.get(id=id)
    image = game.image

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form = form.save(commit=False)
            image = Image.open(form.image)
            box = (0, 0, 200, 200)
            cropped = image.crop(box)
            #form.image = cropped
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
    args['image'] = image

    return render_to_response('editgame.html', args)