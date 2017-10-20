from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        email_val = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        pass_upper = re.compile(r'^.*[A-Z]+.*')
        pass_num = re.compile(r'^.*[0-9]+.*')
        name_val = re.compile(r'^[0-9]+$')

        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors["name"] = "First and last name are required and must be longer than one character"
        elif name_val.match(postData['first_name']) or name_val.match(postData['last_name']):
            errors["name"] = "First and/or last name cannot be just a number"
        elif len(postData['r_email']) < 1 or not email_val.match(postData['r_email']):
            errors["r_email"] = "A valid email address is required"
        elif not pass_upper.match(postData['r_password']) or not pass_num.match(postData['r_password']) or len(postData['r_password']) < 9:
            errors["r_password"] = "Password must be at least 8 characters and have one uppercase letter and one number"
        elif postData['r_password'] != postData['c_password']:
            errors["c_password"] = "Passwords must match"

        return errors;

    def log_validator(self, postData):
        errors = {}

        if len(postData['username']) < 1 or len(postData['password']) < 1:
            errors["login"] = "Email and password are required"

        return errors;


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
