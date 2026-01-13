import threading
import time
import logging

import requests
from django.conf import settings

_logger = logging.getLogger("app1.pinger")
_started = False
_lock = threading.Lock()


def _ping_loop(url: str, interval: int) -> None:
    """Loop that pings `url` every `interval` seconds."""
    while True:
        try:
            resp = requests.get(url, timeout=10)
            _logger.info("Pinged %s (status=%s)", url, resp.status_code)
        except Exception:
            _logger.exception("Ping to %s failed", url)
        time.sleep(interval)


def start_pinger() -> None:
    """Start the background daemon thread that keeps pinging the configured URL.

    Safe to call multiple times; it will only start one thread.
    Respects settings.PING_ENABLED (defaults to True), settings.PING_URL and settings.PING_INTERVAL.
    """
    global _started
    if not getattr(settings, "PING_ENABLED", True):
        _logger.debug("PING disabled in settings; not starting pinger")
        return

    with _lock:
        if _started:
            _logger.debug("Pinger already started")
            return

        url = getattr(settings, "PING_URL", "https://afsal.onrender.com")
        interval = int(getattr(settings, "PING_INTERVAL", 14 * 60))

        t = threading.Thread(target=_ping_loop, args=(url, interval), daemon=True, name="render-pinger")
        t.start()
        _started = True
        _logger.info("Started background pinger for %s every %s seconds", url, interval)
