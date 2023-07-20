from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, LoginForm
from django.contrib import messages
# Create your views here.

def register(request):
    
    # form = UserCreationForm   # eğer sadece bu olursa get metodu çalışmış olur ve sayfada boş form yapısı gelir. eğer formun içini doldurup register butonuna basarsak post metodu devreye girer
    
    form = UserForm()   
    
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)         #bu şekilde register olur olmaz login oluyoruz.
            return redirect('home')
        
            # username = form.cleaned_data.get("username")    bu da register sonrası login olmanın uzun yolu
            # password = form.cleaned_data.get("password2")
            # user = authenticate(username=username, password=password)
            # login(request, user)
    
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def user_login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home') 
    
    context ={
        "form": form
    }
    
    return render(request, 'users/login.html', context)

def user_logout(request):
    logout(request)
    messages.warning(request, 'Logged out successfully')
    return redirect('home')
    
