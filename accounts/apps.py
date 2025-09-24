from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

# FLAW-3
# Missing logging
# FIX for flaw-3, also in signals.py and  mysite/settings.py
# import the signals handler after all the modules are loaded
#     def ready(self):
#         import accounts.signals
