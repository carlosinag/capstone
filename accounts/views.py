from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

# Create your views here.
