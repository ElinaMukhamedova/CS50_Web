from django.shortcuts import HttpResponse

# Create your views here.
def index(request, path):
    return HttpResponse(f"Requested path: {path}")