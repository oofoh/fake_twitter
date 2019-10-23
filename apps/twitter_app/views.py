from django.shortcuts import render, redirect
from apps.login_app.models import *

# Create your views here.
def home_page(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            "logged_user": User.objects.get(id=request.session['id'])
        }
        return render(request, 'twitter_app/home_page.html', context)
        
def explore_page(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'twitter_app/explore.html')

def profile_page(request, profile_name):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            "this_user": User.objects.get(username=profile_name),
            "logged_user": User.objects.get(id=request.session['id'])
        }
        return render(request, 'twitter_app/profile.html', context)

def messages_page(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'twitter_app/messages.html')

def notif_page(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'twitter_app/notifications.html')

def settings_page(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'twitter_app/settings.html')