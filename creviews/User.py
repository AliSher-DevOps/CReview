
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from creviews.sendMails import send_complain_mail, send_mail_reset_password, generate_password


def register_user(request):
    username = request.POST['fullname']
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=username).exists():
        messages.info(request, "*Username Taken*")
        return redirect('signup')
    elif User.objects.filter(email=email).exists():
        messages.info(request, "*Email Address Taken*")
        return redirect('signup')
    context = {
        'title': 'Dashboard',
    }
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    user.save()
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('dashboard')
    return render(request, 'dashboard.html', context=context)


def user_del(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        u = User.objects.get(username=username)
        u.delete()
    return redirect('/')


def send_complain(request):
    first_name = request.POST['first_name']
    fullname = request.POST['full_name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    send_complain_mail(first_name, fullname, email, subject, message)
    return redirect('/')


def reset_account_password(request):
    email = request.POST['recovery_email']
    if User.objects.filter(email=email).exists():
        u = User.objects.get(email=email)
        password = generate_password()
        send_mail_reset_password(email, password)
        u.set_password(password)
        u.save()
        return render(request, 'passwordSetNotification.html')
    else:
        messages.info(request, " Invalid Credentials*")
        return redirect('forget_password')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('dashboard')

    else:
        messages.info(request, "*Invalid Credentials*")
        return redirect('login')
