from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            
            return redirect("home")
        else:
            return render(request, "login.html", 
                {"error": "Username or password is  wrong"
            })
            
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return redirect("home")