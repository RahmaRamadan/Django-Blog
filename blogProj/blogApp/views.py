from ast import Return
from multiprocessing import context
from turtle import title
import re
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.http import HttpResponse
# User Form Imports used in auth
from .forms import CategoryForm, CategoryFormAdmin, UsersForm, PostForm, CommentForm , ReplyForm ,ForbiddenWordForm
# authentications import
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
# models
from .models import Post, User, Comment, Category ,CommentReply ,ForbiddenWord
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# datetime
from django.utils import timezone
from django.contrib.auth.models import Group, User

# Search Feature
def search_menu(request):
    posts = []
    if request.method == 'POST':
        searched = request.POST['searched']
        allposts = Post.objects.all()
        for post in allposts:
            for tag in post.tags.all():
                if searched == tag.name:
                    posts.append(post)
        if len(posts) == 0:
            for post in allposts:
                if searched == post.title:
                    posts.append(post)
        context = {"posts": posts}
        return render(request, 'blogApp/searchtags.html', context)
    else:
        return render(request, 'blogApp/searchtags.html')
# ---------------------------------------------------------------------------------------------

# likePost View
def LikeView(request, post_id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('postDetails', args=[str(post_id)]))

# ---------------------------------------------------------------------------------------------


def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username=name, password=passwd)
            if user is not None:
                if user.groups.filter(name='blocked'):
                    messages.info(request, 'this User is blocked')
                    return render(request, 'blogApp/login.html')
                else:
                    login(request, user)
                    if request.GET.get('next') is not None:
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect('home')
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'blogApp/login.html')

# ---------------------------------------------------------------------------------------------


def signoutPg(request):
    logout(request)
    return redirect('login')

# ---------------------------------------------------------------------------------------------


def signupPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UsersForm()
        if(request.method == 'POST'):
            signup_form = UsersForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + \
                    signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')

        context = {'signup_form': signup_form}
        return render(request, 'blogApp/signup.html', context)

# ---------------------------------------------------------------------------------------------

# Create your views here.
@login_required(login_url='login')
def admin_portal(request):
    current_user = request.user
    print(current_user)
    context = {'usr': current_user}
    if(request.user.is_staff):
        return render(request, 'blogApp/admin-portal.html', context)
    else:
        return render(request, 'blogApp/AUTHORIZATION.html', context)

# ---------------------------------------------------------------------------------------------


def getAllCategories(request):
    categories = []
    all_Categories = Category.objects.all()
    for cat in all_Categories:
        categories.append(cat)
    return categories


# ---------------------------------------------------------------------------------------------
# render home page with current logged user
# Create your views here.
@login_required(login_url='login')
def home(request):
    categories = getAllCategories(request)
    current_user = request.user
    home_posts = Post.objects.all().order_by('-id')
    context = {'usr': current_user,
               'categories': categories, 'home_posts': home_posts}
    return render(request, 'blogApp/home.html', context)

# --------------------------------News Category------------------------------------------------
# get all posts


def catPosts(request, cat):
    cat_posts = Post.objects.all().order_by('-id')
    all_categories = Category.objects.all()
    context = {'cat_posts': cat_posts,
               'cat': cat, 'categories': all_categories}
    return render(request, 'blogApp/catPosts.html', context)

# ---------------------------------------------------------------------------------------------

def redirectCategoryAdd(request, cat):
    catgory_name = cat
    return addFollower(request, catgory_name)


def redirectCategoryRemove(request, cat):
    catgory_name = cat
    return removeFollower(request, catgory_name)

# ---------------------------------------------------------------------------------------------


def addFollower(request, catgory_name):
    log_user = request.user.username
    found = False
    all_categories = Category.objects.all()
    catPosts(request, catgory_name)
    for cat in all_categories:
        if cat.name == catgory_name:
            all_followers = cat.followers.all()
            for follower in all_followers:
                if follower.username == log_user:
                    found = True
                    messages.info(
                        request, "This User Already Exists in This Category")
                    return HttpResponseRedirect(reverse('catPosts', args=[str(catgory_name)]))
                else:
                    found = False
    if found == False:
        Category.objects.get(name=catgory_name).followers.add(request.user)
        messages.info(request, 'Successfully Sunscribed in This Category')
        return HttpResponseRedirect(reverse('home'))

# ---------------------------------------------------------------------------------------------


def removeFollower(request, catgory_name):
    log_user = request.user.username
    found = False
    all_categories = Category.objects.all()

    for cat in all_categories:
        if cat.name == catgory_name:
            all_followers = cat.followers.all()
            for follower in all_followers:
                if follower.username == log_user:
                    found = True
                    Category.objects.get(
                        name=catgory_name).followers.remove(request.user)
                    messages.info(request, "deleted successfully")
                    return HttpResponseRedirect(reverse('home'))
                else:
                    found = False
    if found == False:
        messages.info(request, "this user does not exist in this category")
        return HttpResponseRedirect(reverse('home'))


# ---------------------------------------------------------------------------------------------

def post(request):
    all_posts = Post.objects.all().order_by('-id')
    context = {'all_posts': all_posts}
    return render(request, 'blogApp/post.html', context)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='login')
def users(request):
    users = User.objects.all().order_by('-id')
    print(users)
    context = {'USERS': users}
    return render(request, 'blogApp/users.html', context)
@login_required(login_url='login')
def addAdmin(request, user_id):
    user = User.objects.get(id = user_id) 
    user.is_staff=True 
    user.save()
    return users(request)

@login_required(login_url='login')
def removeAdmin(request, user_id):
    user = User.objects.get(id = user_id) 
    user.is_staff=False 
    user.save()
    return users(request)

@login_required(login_url='login')
def blockUser(request, user_id):
    group = Group.objects.get(name='blocked')
    user = User.objects.get(id=user_id)
    group.user_set.add(user)
    return users(request)


@login_required(login_url='login')
def unblockUser(request, user_id):
    group = Group.objects.get(name='blocked')
    user = User.objects.get(id=user_id)
    group.user_set.remove(user)
    return users(request)

# ---------------------------------------------------------------------------------------------

def postDetails(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogApp/postDetails.html', context)

# ---------------------------------------------------------------------------------------------


@login_required(login_url='login')
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post')

# ---------------------------------------------------------------------------------------------


@login_required(login_url='login')
def addPost(request):
    if(request.method == 'POST'):
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('post')
        else:
            return redirect('home')
    else:
        form = PostForm()
        context = {'form': form, }
        return render(request, 'blogApp/addPost.html', context)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='login')
def addCategory(request):
    if(request.method == 'POST'):
        form = CategoryFormAdmin(request.POST or None, request.FILES or None)
        if form.is_valid():
            Category = form.save(commit=False)
            Category.user = request.user
            Category.save()
            return redirect('admin-portal')
        else:
            return redirect('admin-portal')

    else:
        form = CategoryFormAdmin()
        context = {'form': form, }
        return render(request, 'blogApp/addCategory.html', context)

# ---------------------------------------------------------------------------------------------

@login_required(login_url='login')
def categories(request):
    categories = Category.objects.all().order_by('-id')
    context = {'CATEGORIES': categories}
    return render(request, 'blogApp/categories.html', context)


@login_required(login_url='login')
def editCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    if (request.method == 'POST'):
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            return redirect('home')
    else:
        form = CategoryForm(instance=category)
        context = {'form': form}
        return render(request, 'blogApp/editCategory.html', context)

# --------------------------------------------------------------------------------------------- 

@login_required(login_url='login')
def editCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    if (request.method == 'POST'):
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            return redirect('home')
    else:
        form = CategoryForm(instance=category)
        context = {'form': form}
        return render(request, 'blogApp/editCategory.html', context)

# --------------------------------------------------------------------------------------------- 

@login_required(login_url='login')
def deleteCategory(request, Category_id):
    CategoryVar = Category.objects.get(id=Category_id)
    CategoryVar.delete()
    return redirect('admin-portal')

# ---------------------------------------------------------------------------------------------

@login_required(login_url='login')
def editPost(request, post_id):
    post = Post.objects.get(id=post_id)
    if (request.method == 'POST'):
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
        else:
            return redirect('home')
    else:
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'blogApp/editPost.html', context)

# ---------------------------------------------------------------------------------------------
class AddCommentView(CreateView):
    model = Comment
    template_name = 'blogApp/addComment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        form.instance.date_added = timezone.now()

# ---------------------------------------------------------------------------------------------

        lastoutput=""
        forbidden =ForbiddenWord.objects.all()
        forbiddenList =[]
        for obj in forbidden:
            forbiddenList.append(obj.name)
        print("===========================================",forbiddenList)
        listWords= form.instance.body.split()
        for word in listWords:
            if word in forbiddenList:
                lastoutput += " "
                for i in word:
                   lastoutput += '*'
                lastoutput += " "
            else:
                lastoutput += word
            
        print("===========================================",lastoutput)   
        form.instance.body=lastoutput
        return super().form_valid(form)    
    success_url = reverse_lazy('post')
   
# ---------------------------------------------------------------------------------------------
class addReplyView(CreateView):
    model = CommentReply
    template_name = 'blogApp/addReply.html'
    form_class = ReplyForm
    def form_valid(self,form):
        form.instance.comment_id = self.kwargs['pk']
        form.instance.user = self.request.user
        form.instance.date_added = timezone.now()
        return super().form_valid(form)    
    success_url = reverse_lazy('post')
    # success_url = reverse_lazy('postDetails',kwargs={'post_id':2})


# --------------------------------------------------------------------------------------------- 

def catPosts(request,cat):
    cat_posts = Post.objects.all().order_by('-id')
    context = {'cat_posts': cat_posts,'cat': cat}
    return render(request, 'blogApp/catPosts.html', context)

# --------------------------------------------------------------------------------------------- 

#ForbiddenWord
class addForbiddenWord(CreateView):
    model = ForbiddenWord
    template_name = 'blogApp/addForbiddenWord.html'
    form_class = ForbiddenWordForm
    def form_valid(self,form):
        return super().form_valid(form)    
    success_url = reverse_lazy('post')

