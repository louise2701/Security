from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'home.html', {'user_email': user_email})

def produces(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'produces.html', {'user_email': user_email})

def order_infos(request):
    user_email = request.COOKIES.get('email', None)
    return render(request, 'order_infos.html', {'user_email': user_email})

def confirm_order(request):
    user_email = request.COOKIES.get('email', None)
    # do a post request to confirm the order
    return render(request, 'order_infos.html', {'user_email': user_email})

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def login_submit(request):
    # do a get request to login
    email = 'test@test'

    # if the login is successful
    response = render(request, 'home.html', {'user_email': email})
    response.set_cookie('email', email)
    return response

def signin_submit(request):
    # do a post request to signin
    email = 'test@test'

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