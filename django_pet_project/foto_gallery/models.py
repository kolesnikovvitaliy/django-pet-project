
import os
from django.db import models

def get_upload_path(instance, filename):
    filename = instance.name_foto + '.' + filename.split('.')[1]
    return os.path.join('images/', filename)


class Gallery(models.Model):
    name_foto = models.CharField(max_length=200, verbose_name="Название")
    created_it = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    image = models.ImageField(upload_to=get_upload_path, blank=True, verbose_name="Изображение")

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалерея'

   
    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.name_foto