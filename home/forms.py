from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.forms import fields, widgets

# SignUp Form
class SignupForm(UserCreationForm):
    # Changing fields structure 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}

# Login Form
class LoginForm(AuthenticationForm):
    # Changing fields structure 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

# Change Password Form using Old Password
class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

# Change Password Form without using Old Password
class PasswordForm1(SetPasswordForm):
   new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   
   class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

