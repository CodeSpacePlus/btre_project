from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password != password2:
        messages.error(request, 'Passwords do not match.')
        return redirect('register')

    # Check username
    if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already registerd.')
        return redirect('register')

    # Check email
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email already registered.')
        return redirect('register')

    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                    last_name=last_name)

    # Login after register
    # auth.login(request, user)
    # messages.success(request, 'You are now logged in')
    # return redirect('index')

    user.save()
    messages.success(request, 'You are now registered, please log in to continue.')
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
