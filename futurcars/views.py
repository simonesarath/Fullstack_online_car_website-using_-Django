from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect,reverse,HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Car, Booking,Contact


# Create your views here.

@login_required
def home(request):
    return render(request,"main.html")

def index1(request):
    return render(request,"index1.html")

def index2(request):
    return render(request, "index2.html")

def index3(request):
    return render(request, "index3.html")

def index11(request):
    return render(request, "index11.html")

def index22(request):
    return render(request, "index22.html")

def index33(request):
    return render(request, "index33.html")

# setup in signup  form valid

def signup(request):
    if request.method == 'POST':
        username = request.POST ["username"]
        email = request.POST ["useremail"]
        password = request.POST ["userpassword"]
        confirmpassword = request.POST ["userconfirmpassword"]

        if User.objects.filter(username=username, password=confirmpassword).exists():
            messages.error(request, "Username Is Already Exists. Please Choose A Different Username")

        try:
            user=User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return HttpResponse("Your Account Created Successfully")
        except IntegrityError:
            return HttpResponse("An Error Occurred. Please Try Again.")
    
    return render(request, "main.html")

# setup in login form valid

def login(request):
    if request.method == 'POST':
        email = request.POST ["useremail"]
        password = request.POST ["userpassword"]

        user = authenticate(request, email=email,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invaild Username Or password...")
    return redirect("login")

# contact information for customers
def submit_contact(request):
    if request.method == "POST":
        name = request.POST ['name']
        email = request.POST ['email']
        phonenumber = request.POST ['phonenumber']
        message = request.POST ['message']
        
        contact = Contact(name=name, email=email, phonenumber=phonenumber, message=message)
        contact.save()
        
        return JsonResponse({'success': True, 'success': 'Thank You For Contacting Our Team'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

# The car bookings information
@login_required
def book_car(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponse("Your Car Is Booked Successfully!")
    else:
        form = BookingForm()

    return render(request, 'index1.html', {'form': form})