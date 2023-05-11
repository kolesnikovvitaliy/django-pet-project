from django.contrib import admin
from .models import Gallery


# @admin.register(Gallery)
class Foto_GalleryAdmin(admin.ModelAdmin):
    list_display = ['name_foto', 'created_it', 'image']
    
admin.site.register(Gallery, Foto_GalleryAdmin)
