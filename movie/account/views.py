from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
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
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        password = request.POST.get("password", "")
        repassword = request.POST.get("repassword", "")

        if password != repassword:
            return render(request, "register.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "This email already exists"})

        user = User.objects.create_user(
            username=username,
            email=email, 
            first_name=firstname,
            last_name=lastname, 
            password=password
        )
        user.save()

        return redirect("login")  
    return render(request, "register.html")  



def logout_view(request):
    logout(request)
    return redirect("home")