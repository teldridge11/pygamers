from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from forms import GameForm
from datetime import datetime
import models

@login_required
def userprofile(request):
    return render_to_response('userprofile.html', {'username':request.user.username, 'user':request.user, 'email':request.user.email})

@login_required
def addGame(request):
    user = request.user
    error_message = ""

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
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

    return render_to_response('addGame.html', args)