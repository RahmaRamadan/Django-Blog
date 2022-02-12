from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from .models import Student, Track
# from .forms import StudentForm, UserForm



# Create your views here.
def home(request):
    return render(request,'blogApp/home.html')
