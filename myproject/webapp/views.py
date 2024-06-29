from atexit import register
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm, FeedbackForm, moodForm

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def navbar(request):
    return render(request,'pages/navbar.html')

def about(request):
    return render(request, 'pages/about.html')

def assessment(request):
    return render(request, 'pages/assessment.html')

def moodtracker(request):
    return render(request, 'pages/moodtracker.html')

def contact(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contact')
        
    context = {
        'form':form
    }
  
    return render(request, 'pages/contact.html', context)

def coping(request):
    return render(request, 'pages/coping.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('signin')
        
    context = {
        'form':form
    }
  
    return render(request, 'pages/signup.html', context)

def update(request, pk):
    register = Register.objects.get(id=pk)
    form = SignupForm(instance=register)
    
    if request.method == 'POST':
        form = SignupForm(request.POST, instance=register)
        if form.is_valid():
            form.save()
            return redirect('pro')
        
    context = {'form': form}
    return render(request, 'pages/updateprofile.html', context)

def delete(request, pk):
    register = Register.objects.get(id=pk)
    if request.method == 'POST':
        register.delete()
        return redirect('pro')
    
    context = {'register':register}
    return render(request, 'pages/delete.html', context)

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,  "pages/profile.html", {'fname': fname})
               
        else:
            messages.info(request, "Wrong Username or Password!")
            return redirect('signin')
    return render(request, 'pages/signin.html ')

def signout(request):
    logout(request)
    return redirect('home')

def category(request):
    return render(request, 'pages/category.html')

def person(request):
    return render(request, 'pages/person.html')

def problem(request):
    return render(request, 'pages/problem.html')

def problem1(request):
    return render(request, 'pages/problem1.html')

def updateprofile(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('updateprofile')
        
    context = {
        'form':form
    }
  
    return render(request, 'pages/updateprofile.html', context)

def emotion(request):
    return render(request, 'pages/emotion.html')

def feedback(request):
    feedback = Feedback.objects.all()
    
    context = {
        'feedback': feedback,

        }
    return render(request, 'pages/feedback.html', context)

def meaning(request):
    return render(request, 'pages/meaning.html')

def social(request):
    return render(request, 'pages/social.html')

def avoidance(request):
    return render(request, 'pages/avoidance.html')

def avoidance1(request):
    return render(request, 'pages/avoidance1.html')

def avoidance2(request):
    return render(request, 'pages/avoidance2.html')

def avoidance3(request):
    return render(request, 'pages/avoidance3.html')

def avoidance4(request):
    return render(request, 'pages/avoidance4.html')

def mood(request):
    form = moodForm()
    if request.method == 'POST':
        form = moodForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('mood')
        
    context = {
        'form':form
    }
  
    return render(request, 'pages/mood.html', context)

def pro(request):
    register = Register.objects.all()
    
    context = {
        'register': register,

        }
    return render(request, 'pages/pro.html', context)

def profile(request):
    total = Register.objects.all()
    
    context = {
        'total':total,
    }
    
    return render(request,'pages/profile.html', context)

