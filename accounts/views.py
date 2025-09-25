from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.db import connection #remove flaw-4
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def email_update(request):
    if request.method == "GET":
        return render(request, "email_update.html")
    if request.method == "POST":
        username = request.user
        email = request.POST.get('email')
        # FLAW-4
        # Injection through email update
        sql = f"UPDATE auth_user SET email='{email}' WHERE username='{username}'" #remove flaw-4
        with connection.cursor() as cursor: #remove flaw-4
            cursor.execute(sql) # remove flaw-4
        # FIX for flaw-4, injection through email update:
        # use Django's modules instead to prevent injection
        # user = User.objects.get(username=username)
        # user.email = email
        # user.save()
        return redirect("home")

@login_required
def users(request):
    # FLAW-5, broken access control
    # This page is meant to be accessed only by admins, not regular users
    # Remove lines to fix flaw-5
    users = User.objects.all().values('username', 'email') #remove flaw-5
    return render(request, "users.html", {"users": users}) #remove flaw5
    # End of REMOVE-block

    # FIX for flaw-5:
    # if request.user.is_staff and request.user.is_superuser:
    #    users = User.objects.all().values('username', 'email')
    #    return render(request, "users.html", {"users": users})
    # else:
    #    return HttpResponseForbidden("You are not authorized to see this content.")
    # End of FIX-block