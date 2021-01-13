from django.db import models

# Create your models here.

class Contact(models.Model):
 name = models.CharField(max_length=100)
 email = models.CharField(max_length=100)
 phone = models.CharField(max_length=12)
 desc = models.TextField()
 date = models.DateField()

 def __str__(self):
  return self.name

class Login(models.Model):
 username = models.CharField(max_length=40)
 password = models.CharField(max_length=40)
 date = models.DateField()

 def __str__(self):
  return self.username

class Signup(models.Model):
 username = models.CharField(max_length=40)
 password = models.CharField(max_length=40)
 conferm_password = models.CharField(max_length=40)
 email = models.CharField(max_length=40)
 date = models.DateField()

 def __str__(self):
  return self.username

