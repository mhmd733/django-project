from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index , name = 'index'),
    path ('/shoppingcart', views.cart ,name = 'cart')
]
