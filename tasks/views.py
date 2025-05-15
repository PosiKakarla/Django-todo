from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from tasks.forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'tasks/task_list.html',{'tasks':tasks,'form':form})        
    
def task_toggle(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')