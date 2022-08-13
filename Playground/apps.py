from django.apps import AppConfig


class playgroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'

class storeconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storefront'

class tagsconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags'
