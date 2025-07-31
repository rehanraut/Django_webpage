from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello word I am Yash Thakur")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello yash");

def contact(request):
    return HttpResponse("Hello hareshwar");