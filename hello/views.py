from django.contrib.auth.models import User
from django.db import reset_queries
from django.http import request
from django.shortcuts import render, HttpResponse
from datetime import datetime
from hello.models import Contact, Login, Signup
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')

def fybsc(request):
    return render(request, 'fybsc.html')

def sybsc(request):
    return render(request, 'sybsc.html')

def notice(request):
    return render(request, 'notice.html')


def signup(request):
 if request.method == 'POST':
  username = request.POST['username']
  pass1 = request.POST['pass1']
  pass2 = request.POST['pass2']
  email = request.POST['email']
 
  #Check For Username
  if len(username) > 10:
      messages.error(request, "Username Must Be under 1- Characters")
      return render(request, 'signup.html')

  if not username.isalnum():
      messages.error(request, "Username Should Contain Letter and Numbers")
      return render(request, 'signup.html')
  #Password Checking
  if pass1 != pass2:
      messages.error(request, "Password do not Match")
      return render(request, 'signup.html')

  #Create The User
  myuser = User.objects.create_user(username, email, pass1)
  myuser.save()
  messages.success(request, 'Your Account has been Created')
  return render(request, 'index.html')

 return render(request, 'signup.html')

def handlelogin(request):
 if request.method == 'POST':
  loginusername = request.POST['loginusername']
  loginpassword = request.POST['loginpassword']

  user = authenticate(username= loginusername, password= loginpassword)

  if user is not None:
      login(request, user)
      messages.success(request, "Successfully Logged In")
      return render(request, 'index.html')
  else:
      messages.error(request, "Invalid Credentials, Please Try Again")
      return render(request, 'login.html') 

 return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return render(request, 'index.html')

def forgetpassword(request):
    return render(request, 'forgetpassword.html')
def contact(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     desc = request.POST.get('desc')
     contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
     contact.save()
     messages.success(request, 'Your message has been sent.')

    return render(request, 'contact.html') 


def search(request):
    return HttpResponse('This is search')

def result(request):
    return render(request, 'result.html')

def admission(request):
    return render(request, 'admission.html')

def books(request):
    return render(request, 'books.html')

def department(request):
    return render(request, 'department.html')

def teacher(request):
    return render(request, 'teacher.html')