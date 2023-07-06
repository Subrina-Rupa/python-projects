from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def HomePage(request):
    return render (request,'home.html')
def SignupPage(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        email=request.POST.get('Email')
        pass1=request.POST.get('password')
        cpass=request.POST.get('CPassword')
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        print (uname, email, pass1, cpass)
        return HttpResponse("user has been created sucessfully!!!")
       

    return render (request,'signup.html')
def LoginPage(request):
    return render (request,'login.html')