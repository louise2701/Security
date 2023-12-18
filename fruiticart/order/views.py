from django.http import HttpResponse
from django.shortcuts import render
#from order.models import fruit, vegetable

'''def list_items():
    fruits = fruit.objects.all()
    vegetables = vegetable.objects.all()

    # make a list of fruits and vegetables with their prices that can be send to the html template
    fruits_list = []
    vegetables_list = []
    for f in fruits:
        fruits_list.append([f.name, f.price])
    for v in vegetables:
        vegetables_list.append([v.name, v.price])

    return fruits, vegetables'''

def home(request):
    return render(request, 'home.html')

def produces(request):
    # get the list of fruits and vegetables
    #fruits, vegetables = list_items()
    # send the list of fruits and vegetables to the html template
    return render(request, 'produces.html')

def order_infos(request):
    return render(request, 'order_infos.html')