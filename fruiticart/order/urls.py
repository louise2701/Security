from django.urls import path

from .views import home, produces, order_infos, account, contact, modify_user_info, contact_submit, login_submit, signin_submit, login, signin, logout

urlpatterns = [
    path('home/', home, name='home'),

    path('produces/', produces, name='produces'),

    path('order_infos/', order_infos, name='order_infos'),

    path('account/', account, name='account'),
    path('account/modify_user_info/', modify_user_info, name='modify_user_info'),

    path('login/', login, name='login'),
    path('login/login_submit/', login_submit, name='login_submit'),

    path('signin/', signin, name='signin'),
    path('signin/signin_submit/', signin_submit, name='signin_submit'),

    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
    path('contact/contact_submit/', contact_submit, name='contact_submit')
]