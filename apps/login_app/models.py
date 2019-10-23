from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def account_validator(self, postData):
        errors = {}
        if len(postData['username']) < 1 or len(postData['username']) > 20:
            errors['username'] = "Usernames must be between 1-20 characters."
        email = postData['email']
        if '@' not in email:
            errors['email'] = "Email should be valid."
        if len(postData['first_name']) < 1 or len(postData['first_name']) > 25:
            errors['first_name'] = "First name should be at least 1 character long and not exceed 25 characters."
        if len(postData['last_name']) < 1 or len(postData['last_name']) > 25:
            errors['last_name'] = "Last name should be at least 1 character long and not exceed 25 characters."
        if len(postData['password']) < 4 or len(postData['password']) > 25:
            errors['password'] = "Password should be between 4 and 25."
        if postData['password'] != postData['pw-confirm']:
            errors['pw-confirm'] = "Passwords don't match."
        return errors
        
class User(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=25)
    user_level = models.CharField(max_length=25, default="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f"User object: ID: ({self.id}), {self.first_name} {self.last_name}"