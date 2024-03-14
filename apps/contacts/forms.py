"""Contact Form File"""
from django import forms
from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    """Contact Form class"""
    class Meta:
        """Meta for Model Form"""
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone']
