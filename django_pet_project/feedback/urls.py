from django.urls import path


from .views import create, feedback_form


app_name = 'feedback'

urlpatterns = [
    path('feedback_form', feedback_form, name='feedback_form'),
    path('feedback', create, name='feedback'),
    
]