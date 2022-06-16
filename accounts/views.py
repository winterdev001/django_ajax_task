from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

def userRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account successfully created!')
            return redirect('login')
        context = {
            "page":"register",
            "form" : form,
        }
    else:
        context = {
            "page":"register",
            "form" : UserRegistrationForm()
        }
    return render(request,"auth/register.html",context)

def userLogin(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, 'Signed in successfully.')
            return redirect('index')
        else:
            messages.info(request, f'account does not exist plz Sign up')
    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form':form, })