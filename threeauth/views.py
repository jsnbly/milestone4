from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def logout(request):
    #logout the user
    auth.logout(request)
    messages.success(request,"You have successfully been Logged out")
    return redirect(reverse('index'))
