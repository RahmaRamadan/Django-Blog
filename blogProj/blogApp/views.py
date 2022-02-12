from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
#User Form Imports used in auth
from .forms import UserForm
#authentications import
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

#auth Views here.
def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username= name, password =passwd)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
                
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'blogApp/login.html')

def signoutPg(request):
    logout(request)
    return redirect('login')

def signupPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method =='POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')


        context = {'signup_form': signup_form}
        return render(request, 'blogApp/signup.html', context)
    
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'blogApp/home.html')
