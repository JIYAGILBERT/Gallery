from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . models import Gallery

def main(request):
    return render(request,'index.html')

def login_user(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(main)
        messages.error(request,"Wrong credentials")
        return redirect(login_user)
    return render(request,'index.html')

def signup(request):
    if request.POST:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password == confirmpassword:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect(login_user)
        return redirect(signup)
    return render(request,'signup.html')

def add_user(request):
    if  request.method=='POST' and 'image' in request.FILES:
        myimage = request.FILES['image']
        obj = Gallery(feedimage=myimage)
        obj.save()
        return redirect('add_user')

    #retrive all gallery images to display
    gallery_images = Gallery.objects.all()
    return render(request, "add.html", {"gallery_images":gallery_images})

# Create your views here.


