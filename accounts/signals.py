"""A module handling signals sent by Django"""
import logging
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

logger = logging.getLogger("django.security.LoginFailed")

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
	username = credentials.get('username')
	ip = getattr(request, 'META', {}).get('REMOTE_ADDR')
	logger.warning(
		f"Failed login. User: {username}, IP: {ip}"
	)