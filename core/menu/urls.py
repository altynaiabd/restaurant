from django.urls import path
from . import views

urlpatterns = [
    path(
        'menu-product/',
        views.menu,
        name='menu-product'),

    path(
        'order/', 
        views.order, 
        name='order'),

    path(
        'online-order/',
        views.order,
        name='online_order'),
]