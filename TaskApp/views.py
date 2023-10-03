from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.urls import reverse

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Project.objects.create(name=name, description=description)
        return redirect('project_list')
    return render(request, 'add_project.html')

def remove_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'remove_project.html', {'project': project})

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        project.name = name
        project.description = description
        project.save()
        return redirect('project_list')
    return render(request, 'edit_project.html', {'project': project})
