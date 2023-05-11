
from django.db import models


class Feedback(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    created_it = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'Обратная_связь'
        verbose_name_plural = 'Обратная_связь'


    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email