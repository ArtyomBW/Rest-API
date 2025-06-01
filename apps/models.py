from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.db.models import Model
from django.db.models.fields import DecimalField, TextField, CharField


class Category(Model):
    name = CharField(max_length=255)


class Book(Model):
    title = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=0)
    description = TextField()


