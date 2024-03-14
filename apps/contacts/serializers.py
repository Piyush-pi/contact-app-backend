"""Serializer File"""
from rest_framework import serializers
from apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer"""
    class Meta:
        """Meta Class"""
        model = Contact
        fields = "__all__"
