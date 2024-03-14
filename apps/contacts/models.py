"""Notes app Model File"""
import uuid
from django.db import models


class BaseModel(models.Model):
    """
    Base Model class to add a id, created_at and updated_at field as common
    for all models. properties: id (uuid), created_at, updated_at (timestamp),
    is_deleted
    """
    class Meta:
        """Model Meta class Info."""
        abstract = True

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        """Object String Representation"""
        return f"{self.id}-{self.created_at}"


class Contact(BaseModel):
    """Contact Model"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        """Model Meta class Info."""
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["-created_at"]

    def __str__(self):
        """Object String Representation"""
        return f"{self.id}-{self.first_name}"
