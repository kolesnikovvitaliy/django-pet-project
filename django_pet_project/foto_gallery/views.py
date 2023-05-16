from .models import Gallery
from django.http import HttpResponse
from django.shortcuts import render



def create(request):
    list_foto = Gallery.objects.all()
    return render(request, 'foto_gallery/foto_gallery.html', locals())


   

 

 


     
