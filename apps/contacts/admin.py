"""Django Admin File"""
from django.contrib import admin
from apps.contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact admin class"""
    list_display = ["id", "first_name", "email"]
