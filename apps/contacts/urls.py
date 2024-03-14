"""Contacts URLs"""
from django.urls import path
from apps.contacts.views import (
    ContactListView, ContactCreateView,
    ContactUpdateView, ContactDeleteView
)

app_name = "contacts"

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('add/', ContactCreateView.as_view(), name='contact_create'),
    path('<uuid:id>/edit/', ContactUpdateView.as_view(), name='contact_update'),
    path('<uuid:id>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]
