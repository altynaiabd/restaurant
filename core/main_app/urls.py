from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path(
        'index/',
        views.index,
        name='index'),

    path(
        'gallery/',
        views.gallery,
        name='gallery'),

    path(
        'feedbackandcontacts/',
        views.feedbackandcontacts,
        name='feedbackandcontacts'),

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

    path(
        'reservation/',
        views.reservation,
        name='reservation'),

    path(
        'specialoffers/',
        views.specialoffers,
        name='specialoffers'),

    path(
        'create_payment/', 
        views.create_payment, 
        name='create_payment'),

    path(
        'confrim_payment/', 
        views.confirm_payment, 
        name='confirm_payment'),
]