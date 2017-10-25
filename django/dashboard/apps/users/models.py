from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

email_val = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
pass_val = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
name_val = re.compile(r'^[0-9]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData, level):
        errors = []

        u = self.filter(email=postData['email'])

        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors.append("Your name is required and must be longer than two characters")
        if name_val.match(postData['first_name']) or name_val.match(postData['last_name']):
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
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=hashed,
                level=level
            )
            return new_user
        return errors

    def contact_validator(self, postData, user_id):
        errors = []

        u = self.get(id=user_id)
        e = self.filter(email=postData['email'])

        try:
            level = postData['level']
        except KeyError:
            level = u.level

        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors.append("Your name is required and must be longer than two characters")
        if name_val.match(postData['first_name']) or name_val.match(postData['last_name']):
            errors.append("Name cannot be just a number")
        if len(postData['email']) < 1 or not email_val.match(postData['email']):
            errors.append("A valid email address is required")
        if len(e) > 0:
            if u.email != postData['email']:
                errors.append("That email is already taken")

        if not errors:
            u.first_name=postData['first_name']
            u.last_name=postData['last_name']
            u.email=postData['email']
            u.level=level
            u.save()

            return u
        return errors

    def pswd_validator(self, postData, user_id):
        errors = []

        u = self.get(id=user_id)

        if not pass_val.match(postData['pswd']) or len(postData['pswd']) < 9:
            errors.append("Password must be at least 8 characters and have one uppercase letter, one lowercase letter, and one number")
        if postData['pswd'] != postData['c_pswd']:
            errors.append("Passwords must match")

        if not errors:
            hashed = bcrypt.hashpw(postData['pswd'].encode(), bcrypt.gensalt())

        if not errors:
            u.password=hashed
            u.save()

            return u
        return errors

    def desc_validator(self, postData, user_id):
        errors = []

        u = self.get(id=user_id)

        if len(postData['desc']) < 1:
            errors.append("Please enter a description")

        if not errors:
            u.desc=postData['desc']
            u.save()

            return u
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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    desc = models.TextField()
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
