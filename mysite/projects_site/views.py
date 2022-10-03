from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Project


def index(request):
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects[::-1]}
    return render(request, 'projects_site/index.html', context)


def project_page(request, project_id):
    project_to_show = Project.objects.get(id=project_id)
    context = {'project': project_to_show}
    return render(request, 'projects_site/project.html', context)
