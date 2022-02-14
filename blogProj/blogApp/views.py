from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
#User Form Imports used in auth
from .forms import UserForm , PostForm
from .models import User, Category, Post
#authentications import
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
#models
#auth Views here.
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
# render home page with current logged user
def home(request):
    userDetails(request)
    current_user = request.user
    # name = current_user.username
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
def userDetails(request):
    log_user = request.user.id 
    # all_users = Category.followers.all()
    # context = {'log': log_user}
    all_users = User.objects.values_list('id')
    context = {'users': all_users}
    return render(request, 'blogApp/sports.html', context)
    # context = {'student': loginUser} to send and display user data

    # return render(request,'blogApp/home.html')

def post(request):
    all_posts = Post.objects.all().order_by('-id')
    context = {'all_posts': all_posts}
    return render(request ,'blogApp/post.html',context)

def postDetails(request,post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}
    return render(request ,'blogApp/postDetails.html',context)




def deletePost(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('post')
 
def addPost(request):
    if(request.method == 'POST'):
        form=PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('post')
        else:
            return redirect('home')

    else:
        form=PostForm()
        context={'form' : form}
        return render(request, 'blogApp/addPost.html',context)
 
def editPost(request,post_id):
    post=Post.objects.get(id=post_id)
    if (request.method == 'POST'):
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
        else:
            return redirect('home')
    else:
        form=PostForm(instance=post)
        context={'form' : form}
        return render(request, 'blogApp/editPost.html', context)

