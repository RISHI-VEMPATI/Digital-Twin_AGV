from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        import dashboard.signals  # Import signals to register them