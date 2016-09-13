from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
#from .models import FestemberAdmin
from .forms import LoginForm

# Create your views here.

def login_view(request):
    auth = -1
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username','default_user'),passowrd=request.POST.get('password','default_password'))
            if user is not None:
                login(request,user)
                return redirect('/users/dashboard')
            else:
                form = LoginForm()
                auth = 0
    else:
        form = LoginForm()
    return render(request,'users/login.html',{ 'form' : form, 'auth' : auth })
    
def dashboard(request):
    if request.user.is_authenticated():
        fa = User.objects.get(username = request.user.username)
        return render(request,'users/dashboard.html',{ 'user' : fa })
    else:
        return HttpResponse('Please provide your credentials')
        
def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request,'users/logout.html')
        #return redirect(reverse())
    else:
        return HttpResponse('Please provide your credentials')