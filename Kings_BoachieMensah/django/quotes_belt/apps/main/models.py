from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_user(self, post):
        errors = []

        if len(post.get('name')) == 0:
            errors.append('Name field cannot be empty')
        if len(post.get('alias')) == 0:
            errors.append('Alias field cannot be empty')
        if len(post.get('email')) == 0:
            errors.append('Email field cannot be empty')
        if len(post.get('password')) == 0:
            errors.append('Password field cannot be empty')
        if len(post.get('password')) < 8:
            errors.append('Password must have at least 8 characters')
        if post.get('password') != post.get('confirm_pw'):
            errors.append('Passwords do not match')
        if len(post.get('dob')) == 0:
            errors.append('Date of birth is required')
        if len(errors) == 0:
            return True
        else:
            return errors

    def login_user(self, post):
        user = self.filter(email = post.get('email')).first()
        if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
            return (True, user)
        return (False, 'Please login with the correct username and password')


class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class QuoteManager(models.Manager):
    def validate_quote(self, post):
        errors = []

        if len(post.get('message')) < 10:
            errors.append('Message field must be more than 10 characters')
        if len(post.get('quoted_by')) < 3:
            errors.append('Quoted By field must be more than 3 characters')
        if len(errors) == 0:
            return True
        else:
            return errors


class Quote(models.Model):
    message = models.TextField(max_length = 1000)
    quoted_by = models.TextField(max_length = 1000)
    user = models.ForeignKey(User, related_name = 'quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name = 'favorites')
    quote = models.ForeignKey(Quote, related_name = 'favorites')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
