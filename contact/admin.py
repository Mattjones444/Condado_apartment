# admin.py

from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'check_in', 'check_out', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('submitted_at',)


