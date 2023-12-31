
from django.urls import path, include
from .views import home, pizzas, order_view, my_orders, update_order_view, delete_order_view

urlpatterns = [
    path('', home, name='home'),
    path('pizzas/', pizzas, name='pizzas'),
    path('pizzas/<int:id>', order_view, name='order'),
    path('update_orders/<int:id>', update_order_view, name='update_orders'),
    path('delete_orders/<int:id>', delete_order_view, name='delete_orders'),
    path('my_orders/', my_orders, name='my_orders'),
    
]