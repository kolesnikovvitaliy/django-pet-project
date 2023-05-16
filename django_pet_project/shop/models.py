import os
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    images = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True)
    pris = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

def get_upload_path(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return os.path.join('images/', filename)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products',
        verbose_name="Категория",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=100, db_index=True)
    features = models.TextField(blank=True, verbose_name="Характеристики")  # Empty value
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="Наличие")
    stock = models.PositiveIntegerField(verbose_name="Количество")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    image = models.ImageField(upload_to=get_upload_path, blank=True,
                              verbose_name="Изображение товара")

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_detail',
                        args=[self.id, self.slug])