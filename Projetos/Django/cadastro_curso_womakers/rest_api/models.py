from django.db import models

from django.apps import AppConfig

class RestApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest_api'