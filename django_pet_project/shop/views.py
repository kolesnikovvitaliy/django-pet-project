from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.http import HttpResponse

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query))
        paginator = Paginator(products, len(products) or 100)
    else:
        paginator = Paginator(products, 12)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    # if page.has_previous():
    #     prev_url = '?page={}'.format(page.previous_page_number())
    # else:
    #     prev_url = ''
    
    # if page.has_next():
    #     next_url = '?page={}'.format(page.next_page_number())
    # else:
    #     next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        # 'next_url': next_url,
        # 'prev_url': prev_url,
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def home(request):
    if request.method == 'POST':
        
        data = request.POST.dict()
        subject = f'Сообщение с формы от {data.get("first_name")} Телефон отправителя:'
        context = {}
        email(subject, f'{data.get("fone")}')
    categories = Category.objects.all()
    list_foto = [{'imag':'54865518_2.jpg','nam':'Фруктовый'},
                {'imag':'54857587_2.jpg','nam':'Для девочек'},
                {'imag':'54883095_2.jpg','nam':'Десерт'},
                {'imag':'54868104_2.jpg','nam':'Свадебный'},
                {'imag':'54882693_2.jpg','nam':'Десерты'},
                {'imag':'54712265_3.jpg','nam':'Рулетики'},]
    return render(request, 'shop/home.html', locals(),)


def base(request):
    categories = Category.objects.all()
    return render(request, 'shop/base.html', locals())


def oplata(request):
    categories = Category.objects.all()
    return render(request, 'shop/include/oplata.html', locals())

def contacts(request):
    categories = Category.objects.all()
    return render(request, 'shop/include/contacts.html', locals())





# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'settings.EMAIL_HOST_USER',
      ['admin@django-pet-project.ru']
   )
   return HttpResponse('Письмо отправлено!')


