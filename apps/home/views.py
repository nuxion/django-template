from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the account index")
    return render(request, "home/index.html")

def login_h(request):
    # return HttpResponse("Hello, world. You're at the account index")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

    # return render(request, "home/login.html")
