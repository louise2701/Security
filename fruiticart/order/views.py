from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fruit, Vegetable, Client, Order, Contact

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
        user_info = Client.objects.get(email=user_email)
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
    if 'login_submit' in request.POST:
        # do a get request to login
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check if the email and password are correct
        user = Client.objects.filter(email=email, password=password)
        if not user:
            return render(request, 'login.html', {'error': 'Wrong email or password'})
        else:
            response = redirect('home')
            response.set_cookie('email', email)
            return response

    return render(request, 'login.html')

def signin(request):
    if 'signin_submit' in request.POST:
        # do a post request to signin
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        # check if the email is already used
        user = Client.objects.filter(email=email)
        if user:
            return render(request, 'signin.html', {'error': 'Email already used'})
        else:
            # create the user
            new_user = Client(email=email, password=password, phone_number=phone_number)
            new_user.save()

            # redirect to the home page
            response = redirect('home')
            response.set_cookie('email', email)
            return response

    return render(request, 'signin.html')

def account(request):
    user_email = request.COOKIES.get('email', None)

    # get the user info via the model
    user_info = Client.objects.get(email=user_email)
    # get the user orders via the model
    user_orders = Order.objects.filter(email_id=user_email)

    if 'modify_user_info' in request.POST:
        # get the new user info
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_phone_number = request.POST.get('phone_number')
        new_address = request.POST.get('address')
        new_postal_code = request.POST.get('postal_code')
        new_credit_card = request.POST.get('credit_card')

        # update the user info via the model
        user_info = Client.objects.get(email=user_email)
        user_info.first_name = new_first_name
        user_info.last_name = new_last_name
        user_info.phone_number = new_phone_number
        user_info.address = new_address
        user_info.postal_code = new_postal_code
        user_info.credit_card = new_credit_card
        user_info.save()

        return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders, 'confirm_info': 'User informations modified!'})
    
    if 'change_password' in request.POST:
        # get the old password
        old_password = request.POST.get('old_password')
        # get the new password
        new_password = request.POST.get('new_password')

        # check if the old password is correct
        user = Client.objects.filter(email=user_email, password=old_password)
        if not user:
            return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders, 'error_password': 'Wrong password'})
        else:
            # check if the new password is different from the old one
            if old_password == new_password:
                return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders, 'error_password': 'New password must be different from the old one'})
            else:
                # check that password and confirm password are the same
                confirm_new_password = request.POST.get('confirm_new_password')
                if new_password != confirm_new_password:
                    return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders, 'error_password': 'Password and confirm password must be the same'})
                else:
                    # check that the new password is not empty
                    if new_password == '':
                        return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders, 'error_password': 'Password cannot be empty'})
                    else:
                        # update the user info via the model
                        user_info = Client.objects.get(email=user_email)
                        user_info.password = new_password
                        user_info.save()

                        return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders, 'confirm_password': 'Password changed!'})

    return render(request, 'account.html', {'user_email': user_email, 'user_info': user_info, 'user_orders': user_orders})

def logout():
    # set the cookie to expire
    response = redirect('home')
    response.delete_cookie('email')

    return response

def contact(request):
    user_email = request.COOKIES.get('email', None)

    if 'contact_submit' in request.POST:
        # retrieve the contact info
        name = request.POST.get('name')
        email_contact = request.POST.get('email_contact')
        message = request.POST.get('message')

        # create the message
        new_message = Contact(name=name, email=email_contact, message=message)
        new_message.save()

        return render(request, 'contact.html', {'user_email': user_email, 'confirm': 'Message sent!'})

    return render(request, 'contact.html', {'user_email': user_email})