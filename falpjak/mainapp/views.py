from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SinUpForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, '/mainapp/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'mainapp/login.html')
def sinup_view(request):
    if request.method == 'post':
        form = SinUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sinup_success')
    else:
        form = SinUpForm
        return render (request,'mainapp/sinup.html',{'form':form})    
    

def signup_success(request):
    return render(request, 'signup_success.html')    