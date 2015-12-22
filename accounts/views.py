from django.shortcuts import render_to_response
from forms import MyRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/userprofile/')
    else:
        args = {}
        args.update(csrf(request))
        error_message = "Invalid username or password"
        args['error_message'] = error_message
        #return HttpResponseRedirect('/accounts/login/', args)
        return render_to_response('login.html', args)

def register_user(request):
    error_message = None
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/userprofile/')
        else:
            error_message = "Invalid username or password"

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    args['error_message'] = error_message

    return render_to_response('register.html', args)

def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect('/')