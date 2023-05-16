# from django.views.generic import CreateView
from .models import Feedback
# from django.urls import reverse_lazy
# from .forms import FeedbackForm
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
        # return HttpResponse('Письмо отправлено!')
        # return super().form_valid(form)
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
    # return HttpResponse('Письмо отправлено!')
    # return render(content, 'feedback/succes.html', locals())

def feedback_form(request):
    return render(request, 'feedback/feedback.html', locals())

# Функция, которая вернет сообщение в случае успешного заполнения формы
# def success(request):
#    return HttpResponse('Письмо отправлено!')
   





# def create(request):
#     if request.method == "POST":
#         data = Contact()
#         data.first_name = request.POST.get("first_name")
#         data.fone = request.POST.get("fone")
#         data.email = request.POST.get("mail")
#         data.save()
#         subject = f'django-pet-project {data.id}'

#         message = f'ПОЛЬЗОВАТЕЛЬ {data.first_name} НОМЕР ТЕЛЕФОНА {data.fone} ОТПРАВИЛ ЗАПРОС НА ОБРАТЫЙ ЗВОНОК'
#         connection = get_connection()
#         connection.open()   
#         msg = EmailMultiAlternatives(subject, message,
#                                  settings.EMAIL_HOST_USER, [data.email],
#                                  connection=connection)
#         msg.send()
#         connection.close()  # Cleanup
#     return render(request, 'contact_form/succes.html', locals())


 


     
