from django.urls import path


from .views import create


app_name = 'foto_gallery'

urlpatterns = [
    path('foto_gallery', create, name='foto_gallery'),
    
]