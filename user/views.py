from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başariyla Kayit Oldunuz Hocam")

        return redirect("index")
    context = {
        "form" : form
        }
    return render(request,"register.html",context)
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Kullanici adi veya Parola hatali Tekrar deneyin...")
            return render(request,"login.html",context)
        else:
            messages.success(request,"Hoşgeldin {}, Başariyla giriş yaptin Hocam".format(username))
            login(request,user)
            return redirect("index")
    else:    
        return render(request,"login.html",context)
    

def logoutUser(request):
    logout(request)
    messages.success(request,"başariyla çikiş yaptiniz Hocam...")
    return redirect("index")