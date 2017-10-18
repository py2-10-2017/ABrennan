from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_val = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1:
            errors["name"] = "First and last name are required"
        elif len(postData['email']) < 1 or not email_val.match(postData['email']):
            errors["email"] = "A valid email address is required"

        return errors;

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
