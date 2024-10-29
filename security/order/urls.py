from django.urls import path
from .views import home, project,  login, signin, account, order_history,project_history,project_cartography, logout,product_detail, contact

urlpatterns = [
    path('home/', home, name='home'),

    path('project/', project, name='project'),

   
    path('login/', login, name='login'),

    path('signin/', signin, name='signin'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('account/', account, name='account'),
    path('account/order_history/<int:order_id>/', order_history, name='order_history'),

    path('logout/', logout, name='logout'),

    path('contact/', contact, name='contact'),
    path('project/history/', project_history, name='project_history'),
    path('project/cartography/', project_cartography, name='project_cartography'),
    
]