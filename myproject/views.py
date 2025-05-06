#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("HI THIS IS MY HOMEPAGE")
    return render(request, 'home.html')
def about(request):
    #return HttpResponse("And this is my about page, which is a bit more boring.")
    return render(request, 'about.html')