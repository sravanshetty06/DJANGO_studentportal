from django.apps import AppConfig
import sys
import logging


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        """Start the background pinger unless running management commands where threads are not appropriate."""
        # Avoid starting the background thread during common management commands
        if len(sys.argv) > 1 and sys.argv[1] in (
            'makemigrations', 'migrate', 'collectstatic', 'test', 'shell', 'createsuperuser', 'flush', 'loaddata'
        ):
            return

        try:
            from .pinger import start_pinger
            start_pinger()
        except Exception:
            logging.getLogger(__name__).exception("Failed to start pinger")
