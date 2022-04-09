from django.urls import path
from . import  views


app_name = 'users'
urlpatterns = [
    path('',views.profiles, name='profiles'),
    path('login/',views.loginUser, name='login'),
    path('register/',views.registerUser, name='register'),
    path('account/',views.userAccount, name='account'),
    path('add-skill/',views.addSkill,name='add-skill'),
    path('update-skill/<str:pk>/',views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>',views.deleteSkill,name = 'delete-skill'),
    path('edit-account/',views.editAccount, name='edit-account'),
    path('logout/',views.logoutUser, name='logout'),
    path('profile/<str:pk>',views.userProfile, name= 'profile'),
    path('inbox/',views.inbox, name= 'inbox'),
    path('message/<str:pk>',views.viewMessage, name='message'),
    path('create-message/<str:pk>',views.createMessage,name='crate-message')

]