from django.urls import path
from .views import (Profile, Signup, Login, Logout, ChangePassword, ChangePassword1)

urlpatterns = [
    path('', Profile, name="profile"), # homepage
    path('signup/', Signup, name="signup"), # signup form
    path('login/', Login, name="login"), # login form
    path('logout/', Logout, name="logout"), # logout form
    path('changepass/', ChangePassword, name="changepass"), # change password form
    path('changepass1/', ChangePassword1, name="changepass1"), # change password form 1
]
