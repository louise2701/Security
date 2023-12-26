from django.urls import path
from .views import home, produces, order_infos, confirmation, confirm_order, login, login_submit, signin, signin_submit, account, modify_user_info, change_password, logout, contact, contact_submit

urlpatterns = [
    path('home/', home, name='home'),

    path('produces/', produces, name='produces'),

    path('order_infos/', order_infos, name='order_infos'),
    path('order_infos/confirm_order/', confirm_order, name='confirm_order'),

    path('confirmation/', confirmation, name='confirmation'),

    path('login/', login, name='login'),
    path('login/login_submit/', login_submit, name='login_submit'),

    path('signin/', signin, name='signin'),
    path('signin/signin_submit/', signin_submit, name='signin_submit'),

    path('account/', account, name='account'),
    path('account/modify_user_info/', modify_user_info, name='modify_user_info'),
    path('account/change_password/', change_password, name='change_password'),

    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
    path('contact/contact_submit/', contact_submit, name='contact_submit')
]