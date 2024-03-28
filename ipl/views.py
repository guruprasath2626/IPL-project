from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.


# def admin(request):
    
def admin_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            # else:
            #     error = "Invalid Credentials"
            #     return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})
    


def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def index(request):
    return render(request,'index.html',{})