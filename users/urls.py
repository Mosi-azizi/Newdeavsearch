from django.urls import path
from . import  views


app_name = 'users'
urlpatterns = [
    path('',views.profiles, name='profiles'),
    path('login/',views.loginUser, name='login'),
    path('register/',views.registerUser, name='register'),
    path('account/',views.userAccount, name='account'),
    path('edit-account',views.editAccount, name='edit-account'),
    path('logout/',views.logoutUser, name='logout'),
    path('profile/<str:pk>',views.userProfile, name= 'profile')

]