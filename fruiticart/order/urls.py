from django.urls import path

from .views import home, produces, order_infos, account, contact

urlpatterns = [
    path('home/', home, name='home'),
    path('produces/', produces, name='produces'),
    path('order_infos/', order_infos, name='order_infos'),
    path('account', account, name='account'),
    path('contact/', contact, name='contact')
]