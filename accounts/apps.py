from django.apps import AppConfig

# FIX for flaw-4, also in signals.py and  mysite/settings.py
# class AccountsConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'accounts'

#    def ready(self):
#        import accounts.signals
