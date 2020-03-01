from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            messages.success(request, 'You are successfully logged in')
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid Username or Password or both')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Usernane already exist")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exist")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    user.save()
                    messages.success(
                        request, "You are successfull registered and now can login")
                    return redirect('login')
        else:
            messages.error(request, "Password's do not match")
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    user_id = request.user.id
    inquiries = Contact.objects.all().filter(user_id=user_id)
    context = {
        'inquiries': inquiries
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, 'you are successfully logged out')
    return redirect('index')
