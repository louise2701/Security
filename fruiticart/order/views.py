from django.http import HttpResponse
from django.shortcuts import render

def template0(request):
    return render(request, 'template0.html')

def template1(request):
    return render(request, 'template1.html')

def template2(request):
    return render(request, 'template2.html')