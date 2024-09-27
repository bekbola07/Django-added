from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Home_Page_View(request):
    return render(request, 'index.html')

def Second_Function_View(request):
    return render(request, 'about.html')
