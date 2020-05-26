from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Access Granted')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Wrong Username or Password')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # User Check
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.WARNING, 'This username has already been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.WARNING, 'This email has already been taken')

                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'User Created')
                    return redirect('login')

        else:
            messages.add_message(request, messages.WARNING, 'Passwords are not the same')
            return redirect('register')
    else:
        return render(request, 'user/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Signed Out')
        return redirect('index')
    else:
        return render(request, 'user/logout.html')
