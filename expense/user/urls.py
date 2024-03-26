from django.contrib import admin
from django.urls import path



from .views import UserRegisterView,UserDashboardView
from django.contrib.auth.views import LogoutView , LoginView 
# from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
path('user_register/',UserRegisterView.as_view(),name='userregister'),
#  path('userregister', TemplateView.as_view(template_name='navbar.html'), name='home'),
path('login/',UserLoginView.as_view(),name='login'),
#path('forgot/',UserUpdateView,name='forgot'),
#  path('logout/',LogoutView.as_view(next_page='user/user_dashboard'),name='logout'),
# path("logout/",views.Logoutview,name="logout"),
path('user_dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
# path('forgot-password/', views.forgot_password, name='forgot_password'),
# path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
# path('password-reset-success/', views.password_reset_success, name='password_reset_success'),

# path('safe/',views.safe,name='safe'),
 
 ]