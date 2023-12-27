from django.urls import path
from .views import home, produces, order_infos, confirm_order, order_confirmed, login, signin, account, logout, contact

urlpatterns = [
    path('home/', home, name='home'),

    path('produces/', produces, name='produces'),

    path('order_infos/', order_infos, name='order_infos'),

    path('confirm_order/', confirm_order, name='confirm_order'),
    path('order_confirmed/<int:order_id>/', order_confirmed, name='order_confirmed'),

    path('login/', login, name='login'),

    path('signin/', signin, name='signin'),

    path('account/', account, name='account'),

    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
]