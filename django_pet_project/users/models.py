from django.db import models
from django.contrib.auth.models import User
import io
from django.core.files.storage import default_storage as storage

# from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    phone = models.CharField(max_length=50, verbose_name="Телефон")


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
