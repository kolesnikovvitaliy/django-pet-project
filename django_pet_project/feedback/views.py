from .models import Feedback
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import get_connection, EmailMultiAlternatives
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound


def create(request):
    if request.method == "POST":
       # Сохраняем в базу
        data_model = Feedback()
        data_model.first_name = request.POST.get("first_name")
        data_model.last_name = request.POST.get("last_name")
        data_model.email = request.POST.get("email")
        data_model.message = request.POST.get("message")
        data_model.save()
        # Формируем сообщение для отправки
        subject = f'Сообщение с формы от {data_model.first_name} {data_model.last_name} Почта отправителя: {data_model.email}'
        email(subject, data_model.message)
        return render(request, 'feedback/succes.html', locals())


# Функция отправки сообщения
def email(subject, content):
    connection = get_connection()
    connection.open()
    msg = EmailMultiAlternatives(subject, content,
                                 settings.EMAIL_HOST_USER, ['admin@django-pet-project.ru'],
                                 connection=connection)
    msg.send()
    connection.close()  # Cleanup
    

def feedback_form(request):
    return render(request, 'feedback/feedback.html', locals())


     
