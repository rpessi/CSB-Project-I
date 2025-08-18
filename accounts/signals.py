"""A module handling signals sent by Django"""
# FIX for flaw-4:
# This whole module is part of FIX for flaw-4, imports are not commented
# out in hopes of preventing import errors
# See also apps.py and mysite/settings.py

import logging
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from django.utils import timezone
from django.utils.timezone import localtime

# logger = logging.getLogger("django.security.LoginFailed")

# @receiver(user_login_failed)
# def log_failed_login(sender, credentials, request, **kwargs):
#     username = credentials.get('username')
#     ip = getattr(request, 'META', {}).get('REMOTE_ADDR')
#     time = localtime(timezone.now())
#     timelog = time.strftime("%d-%m-%Y %H:%M:%S")
#     logger.warning(
# 	    f"Failed login. User: {username}, IP: {ip}, time: {timelog}"
#     )