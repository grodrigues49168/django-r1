from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'gabriel rodrigues'})

def sobre(request):
    return HttpResponse('SOBRE - Hello Django')

def contato(request):
    return HttpResponse('CONTATO - Hello Django')
# Create your views here.
