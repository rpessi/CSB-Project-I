from django.urls import path

from .views import SignUpView, email_update


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("email_update", email_update, name="email_update"),
]
