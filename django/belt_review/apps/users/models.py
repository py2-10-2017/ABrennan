from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = []
        email_val = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        pass_val = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
        name_val = re.compile(r'^[0-9]+$')

        u = self.filter(email=postData['email'])

        if len(postData['name']) < 2:
            errors.append("Your name is required and must be longer than two characters")
        if name_val.match(postData['name']):
            errors.append("Name cannot be just a number")
        if len(postData['email']) < 1 or not email_val.match(postData['email']):
            errors.append("A valid email address is required")
        if len(u) > 0:
            errors.append("That email is already taken")
        if not pass_val.match(postData['pswd']) or len(postData['pswd']) < 9:
            errors.append("Password must be at least 8 characters and have one uppercase letter, one lowercase letter, and one number")
        if postData['pswd'] != postData['c_pswd']:
            errors.append("Passwords must match")

        if not errors:
            hashed = bcrypt.hashpw(postData['pswd'].encode(), bcrypt.gensalt())

            new_user = self.create(
                name=postData['name'],
                alias=postData['alias'],
                email=postData['email'],
                password=hashed
            )
            return new_user
        return errors

    def log_validator(self, postData):
        errors = []

        if len(postData['email']) == 0:
            errors.append("Your email is required")

        elif len(self.filter(email=postData['email'])) > 0:
            u = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['pswd'].encode(), u.password.encode()):
                errors.append("Invalid username/password")
        else:
            errors.append("That email does not exist")
        if errors:
            return errors
        return u

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
