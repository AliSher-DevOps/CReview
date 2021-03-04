from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def display_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email

        context = {
            'title': 'Profile',
            'username': username,
            'email': email,

        }
    return render(request, 'profile.html', context=context)


def update_profile(request):
    new_user_name = request.POST['username']
    if User.objects.filter(username=new_user_name).exists():
        messages.info(request, "*Try some other username* ")
        return HttpResponseRedirect('profile')
    user = User.objects.get(username=request.user.username)
    user.username = new_user_name
    user.save()
    messages.info(request, "*Update Profile*")
    return HttpResponseRedirect('profile')


def change_password(request):
    password = request.POST['confPassword']
    if request.user.is_authenticated:
        username = request.user.username
        u = User.objects.get(username=username)
        u.set_password(password)
        u.save()
        messages.info(request, "*Update Password*")
    username = request.user.username
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('profile')
    return HttpResponseRedirect('profile')


