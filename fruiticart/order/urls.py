from django.urls import path
from .views import home, produces, order_infos, confirmation, login, signin, account, logout, contact

urlpatterns = [
    path('home/', home, name='home'),

    path('produces/', produces, name='produces'),

    path('order_infos/', order_infos, name='order_infos'),

    path('confirmation/', confirmation, name='confirmation'),

    path('login/', login, name='login'),

    path('signin/', signin, name='signin'),

    path('account/', account, name='account'),

    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
]