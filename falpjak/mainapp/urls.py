from django.urls import path
from . import views

urlpatterns = [
    path ("login/", views.login_view, name= "login" ),
    path ('sinup/', views.sinup_view,name = 'sinup'),
    path ('sinup_success/', views.signup_success , name='sinup_success'),
]