from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import  Client, Contact, Order, OrderDetail, Product, Fruit, Vegetable
from django.utils import timezone
from django.db import transaction
import json
import datetime

def home(request):
    user_email = request.COOKIES.get('email', None)

    return render(request, 'home.html', {'user_email': user_email})
def product_detail(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        # Retrieve associated fruit or vegetable details
        details = Fruit.objects.filter(product_id=product_id).first() or Vegetable.objects.filter(product_id=product_id).first()

        if details:
            context = {
                'product': product,
                'name': details.name,
                'price': details.price,
                # Add any other details you want to display
            }
            return render(request, 'product_detail.html', context)
        else:
            return HttpResponse("Product not found.", status=404)

    except Product.DoesNotExist:
        return HttpResponse("Product not found.", status=404)
def project_history(request):
    # Placeholder view for project history
    return render(request, 'history.html')  # or return HttpResponse("Project History Placeholder")

def project_cartography(request):
    # Placeholder view for project cartography
    return render(request, 'placeholder.html')  # or return HttpResponse("Project Cartography Placeholder")

def project(request):
    user_email = request.COOKIES.get('email', None)

    # get all the products via the model 
    products_table = Product.objects.all()

    # for each product, get the corresponding fruit or vegetable and its infos
    products = []
    for product in products_table:
        # get the product id
        product_id = product.product_id

        # get the name and price
        tmp = Fruit.objects.filter(product_id=product_id)
        if not tmp:
            tmp = Vegetable.objects.filter(product_id=product_id)
        tmp = tmp[0]

        # add the product to the list of products
        products.append({'product_id': product_id, 'name': tmp.name, 'price': tmp.price})

    # render the page with the products
    return render(request, 'produces.html', {'user_email': user_email, 'products': products})

def order_infos(request):
    user_email = request.COOKIES.get('email', None)

    # if the user is logged, redirect him to the login page, then redirect him to the order_infos page
    if user_email is not None:
        # get the user info via the model
        user_info = Client.objects.get(email=user_email)
        return render(request, 'order_infos.html', {'user_email': user_email, 'user_info': user_info})
    else:
        # redirect the user to the login page with a boolean to know if he comes from the order_infos page
        response = redirect('login')
        response.set_cookie('order_infos', True)
        return response

# function to calculate the total price of the order
def calculate_total_price(cartItems, delivery_option):
    # initialize the total price
    total_price = 0

    for item in cartItems:
        # get the quantity
        quantity = cartItems[item]['quantity']
        # get the product price
        product_price = cartItems[item]['price']

        # calculate the total price
        total_price += product_price * quantity
    
    # add the delivery price
    if delivery_option == 'Express':
        total_price += 5

    return total_price

# temporary route to create the order and then redirect to the order_confirmed page

def order_history(request, order_id):
    user_email = request.COOKIES.get('email', None)

    # get the order infos via the model
    order = Order.objects.get(order_id=order_id)
    # get the order details via the model
    order_details = OrderDetail.objects.filter(order_id=order_id)

    # get the order date
    order_date = order.order_date
    # get the total price
    total_price = order.total_price
    # get the delivery option
    delivery_option = order.delivery_option

    if delivery_option == 'Express':
        delivery_option = True
    else:
        delivery_option = None

    # get the products infos
    products = {}
    for order_detail in order_details:
        # get the product id
        product_id = order_detail.product_id
        # get the quantity
        quantity = order_detail.quantity

        # get the product infos
        tmp = Fruit.objects.filter(product_id=product_id)
        if not tmp:
            tmp = Vegetable.objects.filter(product_id=product_id)
        tmp = tmp[0]

        # add the product to the list of products
        products[product_id] = {'name': tmp.name, 'price': tmp.price, 'quantity': quantity}

    return render(request, 'order_confirmed.html', {'user_email': user_email, 'order_id': order_id, 'order_date': order_date, 'total_price': total_price, 'delivery_option': delivery_option, 'cartItems': products})

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
            if 'order_infos' in request.COOKIES:
                # redirect to the order_infos page
                response = redirect('order_infos')
                response.delete_cookie('order_infos')
            else:
                # redirect to the home page
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

            if 'order_infos' in request.COOKIES:
                # redirect to the order_infos page
                response = redirect('order_infos')
                response.delete_cookie('order_infos')
            else:
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
        new_registered_credit_card = request.POST.get('credit_card')

        # update the user info via the model
        user_info = Client.objects.get(email=user_email)
        user_info.first_name = new_first_name
        user_info.last_name = new_last_name
        user_info.phone_number = new_phone_number
        user_info.address = new_address
        user_info.postal_code = new_postal_code
        user_info.registered_credit_card = new_registered_credit_card
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

def logout(request):
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