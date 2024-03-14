"""Test-cases File"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.contacts.models import Contact


class ContactAPITestCases(TestCase):
    """Contact API Testcases"""
    def setUp(self):
        self.client = APIClient()
        self.contact1 = Contact.objects.create(
            first_name="Joe",
            last_name="Dan",
            email="dan.joe@example.com",
            phone="+1-6549871620",
        )
        self.contact2 = Contact.objects.create(
            first_name="Hello",
            last_name="Parker",
            email="parker.hello@example.com",
            phone="+1-6549871621",
        )

    def test_list_contacts(self):
        """List all contact test-case"""
        response = self.client.get(reverse("contact-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_contact(self):
        """Create Contact test-case"""
        data = {
            "first_name": "Hello",
            "last_name": "Saket 2",
            "email": "saket.hello@example.com",
            "phone": "+1-6791571621",
        }
        response = self.client.post(reverse('contact-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 3)

    def test_retrieve_contact(self):
        """Retrieve Paticular Contact data"""
        response = self.client.get(
            reverse('contact-detail', kwargs={'pk': self.contact1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], "Joe")
        self.assertEqual(response.data['last_name'], "Dan")
        self.assertEqual(response.data['email'], "dan.joe@example.com")
        self.assertEqual(response.data['phone'], "+1-6549871620")

    def test_update_contact(self):
        """Update contact test-case"""
        data = {
            "first_name": "Hello",
            "last_name": "Saket 12",
            "email": "saket.hello.12@example.com",
            "phone": "+1-6791571776",
        }
        response = self.client.put(
            reverse('contact-detail', kwargs={'pk': self.contact1.pk}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get(pk=self.contact1.pk).phone, '+1-6791571776')

    def test_delete_contact(self):
        """Delete contact test case"""
        response = self.client.delete(
            reverse('contact-detail', kwargs={'pk': self.contact1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), 2)
