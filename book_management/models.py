import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token
from Books_Inventory import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class AppUser(AbstractUser, models.Model):
    """
       Model class for manage user details.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Book(models.Model):
    """
        Model class for manage book details.
    """
    book_id = models.CharField(primary_key=True, max_length=100, editable=False)
    book_name = models.CharField(max_length=100, blank=False)
    author_name = models.CharField(max_length=100, blank=False)
    book_count = models.IntegerField(editable=True)

    class Meta:
        db_table = 'book_details'
