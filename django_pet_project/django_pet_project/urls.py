"""
URL configuration for django_pet_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django_pet_project import settings
from cart import views
from shop import views
from users import views as user_views
from contact_form.views import create


urlpatterns = [
    path('admin/', admin.site.urls),
    # 2 path('', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls', namespace='users')),
    # path('paypal/', include('paypal.standard.ipn.urls')),
    # path('payment/', include('payment.urls', namespace='payment')),
    path('order/', include('orders.urls', namespace='orders')),
    path('cupons/', include('cupons.urls', namespace='cupon')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('contact_form/', include('contact_form.urls', namespace='contact_form')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('foto_gallery/', include('foto_gallery.urls', namespace='foto_gallery')),
    path('', include('shop.urls')),
    # path('contact_form/', include('contact_form.urls', namespace='contact_form')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('users/', include('users.urls', namespace='users')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
