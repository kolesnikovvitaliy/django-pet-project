from django.contrib import admin
from django.urls import path
from shop.views import (
    product_list, 
    product_detail,
    home,
    test,
    base,
    # foto,
    oplata,
    contacts,
)

app_name = 'shop'

urlpatterns = [
    path('',home, name='home'),
    path('list', product_list, name='product_list'),
    path('<str:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail'),
    # path('foto', foto, name='foto'),
    path('oplata', oplata, name='oplata'),
    path('contacts', contacts, name='contacts'),
    


]


# path('', views.product_list, name='product_list'),
#     path('elasticsearch_results/', ElasticSearchView.as_view(), name='elasticsearch'),
#     path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
#     path('<str:brand_slug>', views.brands_views, name='brands_views'),
#     path('<str:id>/<str:slug>/', views.product_detail, name='product_detail'),
# path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
#     path('<str:brand_slug>', views.brands_views, name='brands_views'),
#     path('<str:id>/<str:slug>/', views.product_detail, name='product_detail'),


# urlpatterns = [
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_slug>[-\w]+)/$',
#         views.product_list,
#         name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
#         views.product_detail,
#         name='product_detail'),
# ]