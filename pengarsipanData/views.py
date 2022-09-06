from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'home.html'
    context = {
        'title' : 'coba coba',
        'welcome' : 'welcome ges',
    }
    return render(request, template_name, context)
