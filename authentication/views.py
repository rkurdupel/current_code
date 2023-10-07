# Create your views here.
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home_page(request):
    user = request.user 
    print(user)
    print(user.role)
    is_admin = int(user.role) == 1
    return render(request, 'home.html', {"is_admin": is_admin})

def user_page(request):
    return render(request, "user_home.html")

def specific_user_page(request):
    all_users = CustomUser.get_all()
    if request.method == "POST":
        print(1)
        user_id = request.POST.get('user_id')
        user = CustomUser.get_by_id(user_id)
        return render(request, "specific_user.html", {"users": all_users, "user": user})
    
    else:
        
        return render(request, "specific_user.html", {'users': all_users})


def all_users_page(request):
    all_users = CustomUser.get_all()
    return render(request, "all_users.html", {'users': all_users})

def logout_page(request):
    logout(request)
    return redirect('login_page')

def register_page(request):
    
    if request.method == "POST":
        # get data from the form
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if CustomUser.objects.filter(email = email).exists():
            return redirect('error_register')
        else:
            # create a new user
            user = CustomUser.create(
                email=email,
                password=password,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                role=role
            )
            if user:    # if user registered successfully
                return redirect('login_page')
            else:
                return render(request, "register_page.html", {"error_message": "Registration failed"})
    else:
        return render(request, "register_page.html")

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #user = authenticate(request, email = email, password = password)
        try:
            user = CustomUser.objects.get(email = email)
        except CustomUser.DoesNotExist:
            user = None
        
        if user is not None and password == user.password:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, "error")
            return redirect('error_login')
    else:
        return render(request, "login_page.html")

def error_register(request):
    return render(request, "error_register.html")
def error_login(request):
    return render(request, "error_login.html")
