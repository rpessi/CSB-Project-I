from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection #remove flaw-5
from django.urls import reverse_lazy
# FIX for flaw-5, injection through email update:
# from django.contrib.auth.models import User
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
        # FLAW-5
        # Injection through email update
        sql = f"UPDATE auth_user SET email='{email}' WHERE username='{username}'" #remove flaw-5
        with connection.cursor() as cursor: #remove flaw-5
            cursor.execute(sql) # remove flaw-5
        # FIX for flaw-5, injection through email update:
        # use Django's modules instead to prevent injection
        # user = User.objects.get(username=username)
        # user.email = email
        # user.save()
        return redirect("home")