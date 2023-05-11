from django.contrib import admin
from .models import Feedback


# @admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_it', 'email', 'message']
    
admin.site.register(Feedback, FeedbackAdmin)