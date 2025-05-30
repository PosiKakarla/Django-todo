from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'tasks/task_list.html',{'tasks':tasks,'form':form}) 
       
@login_required   
def task_toggle(request,pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def task_delete(request,pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def task_edit(request,pk):
    task=get_object_or_404(Task,pk=pk,user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request,'tasks/task_edit.html',{'form':form,'task':task})        


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})        