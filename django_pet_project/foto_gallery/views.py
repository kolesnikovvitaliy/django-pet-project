# # from django.views.generic import CreateView
from .models import Gallery
# from django.conf import settings
# # from django.urls import reverse_lazy
from django.http import HttpResponse
# from django.core.mail import get_connection, EmailMultiAlternatives
# # from .forms import ContactForm
from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponseNotFound



def create(request):
    # data = Gallery.objects.all()
    # print('DATA = ', data.get('images'))
    list_foto = Gallery.objects.all()
    # print('NUM_IMG', num_img)
    # for foto in data:
    #     list_foto = foto
    #     print(list_foto)
        # product_ids = self.cart.keys()
        # products = Product.objects.filter(id__in=product_ids)
        # for product in products:
        #     self.cart[str(product.id)]['product'] = product

        # for item in self.cart.values():
        #     item['price'] = Decimal(item['price'])
        #     item['total_price'] = item['price'] * item['quantity']
        #     yield item

    return render(request, 'foto_gallery/foto_gallery.html', locals())
#         data = Contact()
#         data.first_name = request.POST.get("first_name")
#         data.fone = request.POST.get("fone")
#         data.email = request.POST.get("mail")
#         data.save()
#         subject = f'TORTIKI-TAGANROG {data.id}'

#         message = f'ПОЛЬЗОВАТЕЛЬ {data.first_name} НОМЕР ТЕЛЕФОНА {data.fone} ОТПРАВИЛ ЗАПРОС НА ОБРАТЫЙ ЗВОНОК'
#         connection = get_connection()
#         connection.open()   
#         msg = EmailMultiAlternatives(subject, message,
#                                  settings.EMAIL_HOST_USER, [data.email],
#                                  connection=connection)
#         msg.send()
#         connection.close()  # Cleanup
#     return render(request, 'contact_form/succes.html', locals())



# # Функция отправки сообщения

   

 

 


     
