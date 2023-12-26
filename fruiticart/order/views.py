from django.http import HttpResponse
from django.shortcuts import render
from .models import Fruit, Vegetable, Client

def home(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'home.html', {'user_email': user_email})

def produces(request):
    user_email = request.COOKIES.get('email', None)

    # get all the products via the model 
    fruits = Fruit.objects.all()
    vegetables = Vegetable.objects.all()

    # render the page with the products
    return render(request, 'produces.html', {'user_email': user_email, 'fruits': fruits, 'vegetables': vegetables})

def order_infos(request):
    user_email = request.COOKIES.get('email', None)

    # get the prices for the products
    fruits = Fruit.objects.all()
    vegetables = Vegetable.objects.all()

    fruits_prices = {}
    for fruit in fruits:
        fruits_prices[fruit.name] = float(fruit.price)
    
    vegetables_prices = {}
    for vegetable in vegetables:
        vegetables_prices[vegetable.name] = float(vegetable.price)

    # if the user is logged, get the user info
    if user_email is not None:
        # get the user info via the model
        user_info = Client.objects.get(mail=user_email)
        return render(request, 'order_infos.html', {'user_email': user_email, 'fruits_prices': fruits_prices, 'vegetables_prices': vegetables_prices, 'user_info': user_info})
    else:
        return render(request, 'order_infos.html', {'user_email': user_email, 'fruits_prices': fruits_prices, 'vegetables_prices': vegetables_prices})

def confirm_order(request):
    user_email = request.COOKIES.get('email', None)
    # do a post request to confirm the order
    return render(request, 'order_infos.html', {'user_email': user_email})

def confirmation(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'confirmation.html', {'user_email': user_email})

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def login_submit(request):
    # do a get request to login
    email = 'test'

    # if the login is successful
    response = render(request, 'home.html', {'user_email': email})
    response.set_cookie('email', email)
    return response

def signin_submit(request):
    # do a post request to signin
    email = 'test'

    # if the login is successful
    response = render(request, 'home.html')
    response.set_cookie('email', email)
    return response

def account(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'account.html', {'user_email': user_email})

def modify_user_info(request):
    user_email = request.COOKIES.get('email', None)
    # do a post request to modify the user info
    return render(request, 'account.html', {'user_email': user_email})

def change_password(request):
    user_email = request.COOKIES.get('email', None)
    # do a post request to change the password
    return render(request, 'account.html', {'user_email': user_email})

def logout(request):
    # set the cookie to expire
    response = render(request, 'home.html')
    response.delete_cookie('email')
    return response

def contact(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'contact.html', {'user_email': user_email})

def contact_submit(request):
    user_email = request.COOKIES.get('email', None)
    # do a post request to send the message
    return render(request, 'contact.html', {'user_email': user_email})