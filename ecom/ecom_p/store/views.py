from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def products(request):
    return render(request,'product.html')
def login(request):
    return render(request,'login.html')
def blogs(request):
    return render(request,'blog_list.html')
def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username==username).exists():
            messages.info(request,"username already exists")
            return redirect('Submit')
        elif User.object.filter(email==email).exists():
            messages.info(request,"email is taken")
            return redirect('Submit')
        else:
          User=User.object.create_user(username==username,email==email,password==password)
          User.save();
          return redirect('/')
    else:
        return render(request,'signup.html')