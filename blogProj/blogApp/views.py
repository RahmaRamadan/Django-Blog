from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
# User Form Imports used in auth
from .forms import UserForm
from .models import User, Category
# authentications import
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# auth Views here.


def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username=name, password=passwd)
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
        if(request.method == 'POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + \
                    signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')

        context = {'signup_form': signup_form}
        return render(request, 'blogApp/signup.html', context)

# Create your views here.


@login_required(login_url='login')
#render home page with current logged user
def home(request):
    current_user = request.user
    context = {'usr': current_user}
    
    return render(request, 'blogApp/home.html', context)


@login_required(login_url='login')
def redirectNews(request):
    return render(request, 'blogApp/news.html')


@login_required(login_url='login')
def redirectSports(request):
    return render(request, 'blogApp/sports.html')


@login_required(login_url='login')
def redirectPolitics(request):
    return render(request, 'blogApp/politics.html')

@login_required(login_url='login')
def userDetails(request, usr_id):
    loginUser = User.objects.get(id=usr_id)
    all_user = Category.followers
    # context = {'student': loginUser} to send and display user data
    # return render(request, 'dj_app/details.html', context)



# @login_required(login_url='login')
# def addStudent(request):
#     if request.method == 'POST':
#         form = StudentsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     form = StudentsForm()
#     context = {'form': form}
#     return render(request, 'dj_app/add.html', context)
