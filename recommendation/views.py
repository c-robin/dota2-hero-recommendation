from django.shortcuts import render
from django.http import HttpResponse
from . import tasks
# Create your views here.

def home(request):
    tasks.logger.delay()
    return HttpResponse()
    
    
def update_hero(request):
    tasks.update_hero.delay()
    return HttpResponse()