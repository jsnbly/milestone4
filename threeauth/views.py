from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from threeauth.forms import UserLoginForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def logout(request):
    #logout the user
    auth.logout(request)
    messages.success(request,"You have successfully been Logged out")
    return redirect(reverse('index'))

def login (request):
    #login page
    #login_form = UserLoginForm()
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

        if user:
            auth.login(user=user,request=request)
            messages.success(request,"You have successfully logged in...")
        else:
            login_form.add_error(None,"Your Username or Password was Incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form" : login_form})
