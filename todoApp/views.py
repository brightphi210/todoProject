from django.shortcuts import render, redirect
from .models import TodoModel
from .form import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your vdecorators import login_requirediews here.


def home(request):
    return render(request, 'main.html')


def signupView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logoutView(request):
    logout(request)
    return redirect('/')

@login_required
def create_get(request):
    
    # ========= GET ALL DATA FROM MYTODO MODEL ======= 
    todos = TodoModel.objects.all().order_by('-id')

    if request.method == 'POST':
        frontTitle = request.POST.get('frontTitle')
        newTitle = TodoModel.objects.create(title=frontTitle)
        newTitle.save()
        
    return render(request, 'home.html', {'todos':todos})

@login_required
def update_todo(request, pk):
    todo = TodoModel.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('newTitle')
        todo.save()
        return redirect('/')
    return render(request, 'update.html', {'todo':todo})

@login_required
def delete_todo(request, pk):
    todo = TodoModel.objects.get(pk=pk)
    todo.delete()
    return redirect('/')


