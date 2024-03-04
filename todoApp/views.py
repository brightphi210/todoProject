from django.shortcuts import render, redirect
from .models import TodoModel
# Create your views here.

def create_get(request):
    
    # ========= GET ALL DATA FROM MYTODO MODEL ======= 
    todos = TodoModel.objects.all().order_by('-id')

    if request.method == 'POST':
        frontTitle = request.POST.get('frontTitle')
        newTitle = TodoModel.objects.create(title=frontTitle)
        newTitle.save()
        
    return render(request, 'home.html', {'todos':todos})

def update_todo(request, pk):
    todo = TodoModel.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('newTitle')
        todo.save()
        return redirect('/')
    return render(request, 'update.html', {'todo':todo})


def delete_todo(request, pk):
    todo = TodoModel.objects.get(pk=pk)
    todo.delete()
    return redirect('/')