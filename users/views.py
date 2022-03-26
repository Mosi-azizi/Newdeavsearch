from django.shortcuts import render, redirect
from .models import Profile,Skill
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .form import CustomUserCreationFrom,ProfileForm
# Create your views here.



def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('users:profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User dose not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:profiles')
        else:
            messages.error(request,'username or pass incorrect')

    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request,'User was logged out!')
    return redirect('users:login')



def registerUser(request):
    page = 'register'
    form = CustomUserCreationFrom()

    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User save')
            login(request, user)
            return  redirect('users:edit-account')
        else:
            messages.error(request,'An error has occurred during registrations' )


    context= {
        'page': page,'form':form
    }
    return  render(request,'users/login_register.html',context)



def profiles(request):

    profiles = Profile.objects.all()
    skills = Skill.objects.all()

    context = {
        'developers':profiles,
        'skills':skills
    }
    return render(request,'users/profiles.html',context)


# @login_required(login_url='users:login')
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills
    }
    return render(request,'users/user-profile.html',context)


@login_required(login_url='users:login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile':profile,'skills':skills,
        'projects':projects
    }
    return render(request,'users/account.html',context)

@login_required(login_url='users:login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            return redirect('users:account')
            messages.success(request,'Users has been edited')
        else:
            messages.error(request,'sdfsdf')

    context = {
        'form':form
    }
    return  render(request,'users/profile_form.html',context)