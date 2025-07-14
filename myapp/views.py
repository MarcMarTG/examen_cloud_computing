from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST   
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
from django.db.models import Count  # para contar tareas
from django.views.decorators.http import require_http_methods

def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)




def projects(request):
    query = request.GET.get('q', '')
    if query:
        projects = Project.objects.filter(name__icontains=query)
    else:
        projects = Project.objects.all()
    # Anotar con la cantidad de tareas por proyecto (para contador)
    projects = projects.annotate(task_count=Count('task'))
    return render(request, 'projects/projects.html', {
        'projects': projects,
        'query': query,
    })



def tasks(request):
    # task = Task.objects.get(title=tile)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            project = form.cleaned_data['project']
            Task.objects.create(title=title, description=description, project=project)
            return redirect('tasks')
        else:
            return render(request, 'tasks/create_task.html', {
                'form': form
            })



def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })

def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'GET':
        form = CreateNewProject(instance=project)
        return render(request, 'projects/edit_project.html', {'form': form, 'project': project})
    else:
        form = CreateNewProject(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        return render(request, 'projects/edit_project.html', {'form': form, 'project': project})




@require_http_methods(["GET", "POST"])
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/confirm_delete.html', {'project': project})


@require_POST
def task_delete(request, id):

    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks')

@require_POST
def task_done(request, id):

    task = get_object_or_404(Task, id=id)
    task.done = True         
    task.save()
    return redirect('tasks')