from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SinUpForm(UserCreationForm):
    email = forms.EmailField(max_length = 65,  help_text= 'Required. inform vailed email address')

    class Mate :
        model = User
        field = ('username','email','password1','password2')