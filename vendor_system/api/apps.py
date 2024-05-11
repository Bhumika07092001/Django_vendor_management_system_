from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
      import api.signals 
