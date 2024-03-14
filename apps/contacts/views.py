"""View File"""
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.contacts.serializers import ContactSerializer
from apps.contacts.models import Contact
from apps.contacts.constants import ApplicationMessages
from apps.contacts.forms import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    """Contacts Viewset"""
    serializer_class = ContactSerializer

    def get_queryset(self):
        """Get queryset"""
        queryset = Contact.objects.filter(is_deleted=False)
        return queryset

    def create(self, request):
        """Create Contact"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve Contact"""
        try:
            contact = get_object_or_404(Contact, pk=pk)
            serializer = self.get_serializer(contact)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            error = {"error": ApplicationMessages.CONTACT_NOT_FOUND}
            return Response(error, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update Contact Info."""
        try:
            contact = get_object_or_404(Contact, pk=pk)
            serializer = self.get_serializer(contact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Contact.DoesNotExist:
            error = {"error": ApplicationMessages.CONTACT_NOT_FOUND}
            return Response(error, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Delete Contact"""
        try:
            contact = get_object_or_404(Contact, pk=pk)
            contact.is_deleted = True
            contact.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            error = {"error": ApplicationMessages.CONTACT_NOT_FOUND}
            return Response(error, status=status.HTTP_404_NOT_FOUND)


class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'


class ContactCreateView(CreateView):
    """Contact Create View"""
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:contact_list')


class ContactUpdateView(UpdateView):
    """Contact Update View"""
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:contact_list')


class ContactDeleteView(DeleteView):
    """Contact Delete View"""
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = reverse_lazy('contacts:contact_list')
