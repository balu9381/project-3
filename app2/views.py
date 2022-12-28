from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ravi(request):
    return HttpResponse('<h1><marquee>this is app2 first view</marquee></h1>')

def teja(request):
    return HttpResponse('<h1><marquee>this is app2 second view</marquee></h1>')
