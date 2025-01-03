from django.shortcuts import render, redirect
from .models import Gallery

def index(request):
    if  request.method == 'POST' and 'Image' in request.FILES:
        myimage = request.FILES['image']
        obj = Gallery(feedimage=myimage)
        obj.save()
        return redirect('index')

    #retrive all gallery images to display
    gallery_image = Gallery.objects.all()
    return render(request, "index.html", {"gallery_images":gallery_image})

# Create your views here.
