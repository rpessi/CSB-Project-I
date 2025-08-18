from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
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
        sql = f"UPDATE auth_user SET email='{email}' WHERE username='{username}'"
        with connection.cursor() as cursor:
            cursor.execute(sql)

        return redirect("home")