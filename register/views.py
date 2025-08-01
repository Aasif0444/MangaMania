from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateUser
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def loginPage(response):    
    form = response.POST    
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')

        user = authenticate(response,username=username,password=password)
        if user is not None:
            login(response,user)
            return redirect('homepage')

    return render(response,'register/LoginPage.html',{})

def registration(response):
    form = CreateUser()

    if response.method == 'POST':
        form = CreateUser(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('urser created')

    return render(response,'register/RegisterationPage.html',{'form':form})



