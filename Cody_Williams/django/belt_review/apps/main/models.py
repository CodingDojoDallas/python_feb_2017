from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def login_user(self, post):
		user = self.filter(email=post.get('email')).first()
		if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
			return (True, user)
		else:
			return (False)

class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
	review = models.TextField()
	score = models.IntegerField()
	book = models.ForeignKey(Book, related_name='reviews')
	user = models.ForeignKey(User, related_name='reviews')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)








