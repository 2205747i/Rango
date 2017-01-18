

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!" "<html> <a href='/rango/about/'>About</a>.</html>")

def about(request):
    return HttpResponse("Rango says here is the about page." "<html> <a href='/rango'>Index</a>.</html>")
