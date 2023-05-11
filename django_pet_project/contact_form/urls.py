from django.urls import path


from .views import create


app_name = 'contact_form'

urlpatterns = [
    path('contact_form', create, name='contact_form'),
    
]