from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Views are the webpages that display, which connect to the mysite server.
# Create your views here. 

def index(response, id):
    ls = ToDoList.object.get(id=id)
    return render(response, "main/base.html",{}) 
    #Returns HTML code to the screen

def v1(response):
    return HttpResponse("<h1>v1 home</h1>") 
    #Returns HTML code to the screen
