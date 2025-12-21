"""
Keep-Alive Management Command
This pings the application every 14 minutes to prevent Render from sleeping.
"""
import requests
import time
import os
from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler

class Command(BaseCommand):
    help = 'Keeps the Render service alive by self-ping every 14 minutes'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        
        def ping_self():
            """Ping function to keep the service awake"""
            app_url = os.environ.get('RENDER_EXTERNAL_URL', 'http://localhost:8000')
            try:
                response = requests.get(f'{app_url}/', timeout=30)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'[Keep-Alive] Ping successful: {response.status_code}'
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(
                        f'[Keep-Alive] Ping failed: {str(e)}'
                    )
                )
        
        # Schedule ping every 14 minutes (Render sleeps after 15 minutes of inactivity)
        scheduler.add_job(ping_self, 'interval', minutes=14)
        scheduler.start()
        
        self.stdout.write(
            self.style.SUCCESS(
                'Keep-Alive service started. Pinging every 14 minutes...'
            )
        )
        
        # Keep the script running
        try:
            while True:
                time.sleep(60)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()
            self.stdout.write(
                self.style.WARNING('Keep-Alive service stopped.')
            )
