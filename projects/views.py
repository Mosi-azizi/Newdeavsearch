from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects,paginateProjects


# Create your views here.

def Home(request):

    context ={

    }
    return render(request,'home.html',context)

def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)

    context ={
        'projects':projects,'search_query':search_query,'custom_range':custom_range
    }
    return render(request, 'projects/projects.html', context)



def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()
    context={
        'projectObj':projectObj,
        # 'tags':tags
    }
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='users:login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.POST)
            project = form.save(commit=False)
            project.owner = profile
            project.save()


            return redirect('users:account')
    context = {
        'form':form
    }
    return render(request,'projects/project_form.html',context)


@login_required(login_url='users:login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('users:account')
    context = {
        'form':form
    }
    return  render(request,'projects/project_form.html',context)


@login_required(login_url='users:login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:projects')
    context = {
        'object':project
    }
    return  render(request,'delete_template.html',context)