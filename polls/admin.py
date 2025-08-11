from django.contrib import admin

# imports for checking user and getting access to
# environmental variables
from django.contrib.auth import get_user_model
from django.conf import settings

from .models import Question, Choice

User = get_user_model()

username = 'admin'
password = getattr(settings, 'ADMIN_PW', None)

try:
  admin_user = User.objects.get(username=username)
  admin_user.set_password(password)
  admin_user.save()
except User.DoesNotExist:
  User.objects.create_superuser(
    username=username,
    email="admin@example.com",
    password=password
  )

# The presence of admin user in database is first checked.
# If present, the password is updated by using the environmental
# constant, which is read from .env file. If there's no admin
# user, one is created. This way of updating the admin password
# is not advisable, as environmental variables are leaked to
# browser with DEBUG = True and poor exception handling. Superusers
# can be created using manage.py CLI.
# Fix: remove imports for get_user_model and settings, remove all
# code for checking if admin is created and updating admin password

admin.site.register(Question)
admin.site.register(Choice)
