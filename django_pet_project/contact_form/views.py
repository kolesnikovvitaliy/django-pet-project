# from django.views.generic import CreateView
from .models import Contact
from django.conf import settings
# from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import get_connection, EmailMultiAlternatives
# from .forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound



def create(request):
    if request.method == "POST":
        data = Contact()
        data.first_name = request.POST.get("first_name")
        data.fone = request.POST.get("fone")
        data.email = request.POST.get("mail")
        data.save()
        subject = f'django-pet-project {data.id}'

        message = f'ПОЛЬЗОВАТЕЛЬ {data.first_name} НОМЕР ТЕЛЕФОНА {data.fone} ОТПРАВИЛ ЗАПРОС НА ОБРАТЫЙ ЗВОНОК'
        connection = get_connection()
        connection.open()   
        msg = EmailMultiAlternatives(subject, message,
                                 settings.EMAIL_HOST_USER, [data.email],
                                 connection=connection)
        msg.send()
        connection.close()  # Cleanup
    return render(request, 'contact_form/succes.html', locals())



# Функция отправки сообщения

   

 

 


     
