from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Subscribe
from django.contrib import messages


def subscribe(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']

        if name and email:
            if Subscribe.objects.filter(name=name).exists():
                messages.error(
                    request, "you have already subscribed with this name")
                return redirect('index')

            if Subscribe.objects.filter(email=email).exists():
                messages.error(
                    request, "you have already subscribed with this email")
                return redirect('index')

            elif request.user.is_authenticated:
                messages.error(
                    request, "No need to subscribe, you are already a user")
                return redirect('index')

            elif User.objects.filter(username=name).exists():
                messages.error(
                    request, "Username already exist as user")
                return redirect('index')

            elif User.objects.filter(email=email).exists():
                messages.error(
                    request, "Email already exist as user")
                return redirect('index')

            else:
                subscribe = Subscribe(name=name, email=email)
                subscribe.save()
                messages.success(
                    request, "Congratulation You have been subscribed")
                return redirect('index')
        else:
            messages.error(request, "No Name And Email")
            return redirect('index')
