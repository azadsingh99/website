from django.contrib import admin

from hello.models import Contact, Login, Signup
# Register your models here.

admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Signup)
