from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):

    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
	    form = TaskForm(request.POST) #pass post method
	    if form.is_valid():
		    form.save()	#saves to the database
	    return redirect('/') #send back to same url path

    context = {'tasks': tasks, 'form': form}

    return render(request, 'todoapp/list.html', context)


def updateTask(request, pk): #pk is a url pattern
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
	    form = TaskForm(request.POST, instance=task) #pass post method
	    if form.is_valid():
		    form.save()	#saves to the database
	    return redirect('/') #send back to same url path

    context = {'form': form}
    
    return render(request, 'todoapp/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
        
    context = {'item': item}
    
    return render(request, 'todoapp/delete.html', context)

