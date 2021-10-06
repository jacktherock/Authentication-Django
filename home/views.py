from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from .forms import SignupForm, LoginForm, PasswordForm, PasswordForm1

# Profile View
def Profile(request):
    if request.user.is_authenticated: # 1 if user is login then only show profile page
        return render(request, 'profile.html', {'name':request.user})
    else: # 1.1 else redirect to login page
        return HttpResponseRedirect('/login/')

# Signup view
def Signup(request):
    if not request.user.is_authenticated: # 1 if user is not signup then only redirect to 'signup'
        if request.method=='POST': # 2 if user's request method is POST then only submit signup form
            fm = SignupForm(request.POST)
            if fm.is_valid(): # if given info is valid then save form in User model & redirect to login page
                fm.save()
                messages.success(request, "Account Created Successfully! Please Login !")
                return HttpResponseRedirect('/login/')
        else: # 2.2 else give blank signup form
            fm = SignupForm()
    else: # 1.1 else redirect to homepage
        return HttpResponseRedirect('/')
    context = {'form':fm}
    return render(request, 'signup.html', context)

# Login View
def Login(request):
    if not request.user.is_authenticated: # 1 if user is not login then only redirect to 'login'
        if request.method=='POST': # 2 if user's request method is POST then only login
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None: # 3 if user's credentials are present in User model form then only redirect to homepage and show user details
                    login(request, user)
                    messages.success(request, "Logged In Successfully!")
                    return HttpResponseRedirect('/')
        else: # 2.2 else give blank login form
            fm = LoginForm()
    else: # 1.1 else redirect to homepage
        return HttpResponseRedirect('/')
    context = {'form':fm}
    return render(request, 'login.html', context)

# Logout View
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change Password using old Password:
def ChangePassword(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password Changed Successfully!")
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/')
        else:
            fm = PasswordForm(user=request.user)
    else:
        return HttpResponseRedirect('login')
    context = {'form':fm}
    return render(request, 'changepassword.html', context)

def ChangePassword1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PasswordForm1(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password Changed Successfully!")
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/')
        else:
            fm = PasswordForm1(user=request.user)
    else:
        return HttpResponseRedirect('/login/')
    context = {'form':fm}
    return render(request, 'changepassword1.html', context)