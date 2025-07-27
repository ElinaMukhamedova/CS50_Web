from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def hope(request):
    return HttpResponse("Hello, Elina!")

def trust(request):
    return HttpResponse("Hello, Vera!")

def love(request):
    return HttpResponse("Hello, Elvira!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })