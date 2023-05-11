from django.contrib import admin
from .models import Contact


# @admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'fone', 'created_it', 'email']
    
admin.site.register(Contact, ContactAdmin)
