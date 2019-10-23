from django.shortcuts import render, redirect
from apps.login_app.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user' not in request.session:
        return render(request, 'login_app/index.html')
    else:
        return redirect('/home')

def register(request):
    if 'user' not in request.session:
        return render(request, 'login_app/register.html')
    else:
        return redirect('/home')

def register_new(request):
    errors = User.objects.account_validator(request.POST)
    all_users = User.objects.all()
    for user in all_users:
        if user.username == request.POST['username'] and user.email == request.POST['email']:
            errors['username-exists'] = "Username already exists"
            errors['email-exists'] = "Email is already in use"
            break
        if user.username == request.POST['username']:
            errors['username-exists'] = "Username already exists"            
            break
        if user.email == request.POST['email']:
            errors['email-exists'] = "Email is already in use"            
            break
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    if request.POST['password'] == request.POST['pw-confirm']:
        new_user = User.objects.create(username=request.POST['username'], email=request.POST['email'], first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], password=request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/')
    else:
        return redirect('/register')

def login(request):
    if User.objects.filter(username=request.POST['login-username']).exists():
        logged_user = User.objects.filter(username = request.POST['login-username'])
        if logged_user[0]:
            if logged_user[0].password == request.POST['login-password']:
                request.session['user'] = logged_user[0].first_name
                request.session['id'] = logged_user[0].id
                return redirect('/home')
            else:
                messages.error(request, "Invalid account credentials")
                return redirect('/')
    else:
        messages.error(request, "Invalid account credentials")
        return redirect('/')
 
def logout(request):
    request.session.flush()
    return redirect('/')