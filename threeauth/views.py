from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from threeauth.forms import UserLoginForm, UserRegistrationForm
# Create your views here.

def index(request):
    return render(request, 'threeauth/index.html')

@login_required(login_url='/auth/login')
def logout(request):
    #logout the user
    auth.logout(request)
    messages.success(request,"You have successfully been Logged out")
    return render(request, 'threelite/index.html')

def login (request):
    #login page
    #login_form = UserLoginForm()
    if request.user.is_authenticated:
        return render(request, 'threelite/index.html')
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

        if user:
            auth.login(user=user,request=request)
            messages.success(request,"You have successfully logged in...")
            return render(request, 'threelite/index.html')
        else:
            login_form.add_error(None,"Your Username or Password was Incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'threeauth/login.html', {"login_form" : login_form})

def register(request):
    #user registration 
    if request.user.is_authenticated:
        return render(request, 'threelite/index.html')
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request,"You have successfully Registered")
                return render(request,'threeauth/registration.html')
            else:
                messages.error(request, "Unable to register you account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'threeauth/registration.html', {"registration_form": registration_form}) 


def user_profile(request):
    #users profile page
    user = User.objects.get(email=request.user.email)
    return render(request, 'threeauth/profile.html', {"profile":user})
