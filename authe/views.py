from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        # user1=authenticate(username=username,password=password)
        user=User.objects.get(username=username,password=password)
        print(user.username,user.password)

        # if user1 is not None:
        #     login(request,user1)
        #     return redirect('home')
        
        # if username==user.username and password==user.password:
        #     login(request,user)
        #     return redirect('home')
        # else:
        #     return HttpResponse('Invalid username or password!')

        try:
            user=User.objects.get(username=username)
        except: 
            return HttpResponse("username doesnot exist")
        if user.password==password:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('wrong credentials')
    return render(request,'login_.html')

def register_(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print(username,email,password)
        User.objects.create(username=username,email=email,password=password)
        # u.set_password(password)
        # u.save()
        return redirect('login_')
    return render(request,'register.html')

def logout_(request):
    logout(request)
    return redirect('login_')