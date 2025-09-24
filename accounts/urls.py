from django.urls import path

from .views import SignUpView, email_update, users


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("email_update", email_update, name="email_update"),
    path("users", users, name="users"),
]
