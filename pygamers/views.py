from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    return render_to_response('base.html', )

def home_page(request):
    return render_to_response('homepage.html', {'username':request.user.username, 'user':request.user, 'email':request.user.email})