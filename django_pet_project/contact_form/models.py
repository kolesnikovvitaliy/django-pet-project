from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    fone = models.CharField(max_length=200)
    created_it = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

   
    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.first_name