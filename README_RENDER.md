# Deploying to Render.com

Steps to deploy this Django project to Render:

1. Push your repository to GitHub (already done).
2. Log in to Render (https://render.com) and create a new **Web Service**.
   - Connect your GitHub account and select this repository.
   - Environment: **Python**
   - Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn studentdata.wsgi:application --bind 0.0.0.0:$PORT`
3. Add environment variables in Render dashboard (Environment > Environment Variables):
   - `SECRET_KEY` = <your secret key>
   - `DATABASE_URL` = <postgres connection string> (If you add a Render Postgres add-on, Render will set this automatically.)
   - `DJANGO_DEBUG` = `False`
   - Optionally `ALLOWED_HOSTS` = `your-app.onrender.com` (or `*` for convenience)
   - `SECURE_HSTS_SECONDS` = `31536000` (optional; enable only when you are ready to enforce HSTS)

**Security note:** Ensure your `SECRET_KEY` is a long, random value (not the default `django-insecure-...`). Django will warn if your `SECRET_KEY` is insecure—set it as an environment variable in Render.
4. (Optional) Add a Postgres database from Render and copy the `DATABASE_URL` into the service env vars.
5. Deploy — monitor the build logs and fix any errors if they appear.

Render YAML: This repo includes `render.yaml` so you can create the service via Git by rendering a Service file if you prefer infra-as-code.

## Keep‑alive pinger (self‑ping) 🔁
This project includes a small background daemon that periodically sends an HTTP GET to the service's public URL to help keep free Render instances awake.

- It is started automatically at app startup by `app1.apps.App1Config.ready()` (it avoids running during common management commands).
- Environment variables:
  - `PING_ENABLED` (True/False) — default: `True` (set to `False` to disable)
  - `PING_URL` — default: `https://afsal.onrender.com` (replace with your actual Render URL)
  - `PING_INTERVAL_SECONDS` — default: `840` (14 minutes). When `DJANGO_DEBUG=True` the default is `30` seconds to make local testing faster.
- Logs are emitted via the `app1.pinger` logger and will appear on the console (or Render logs).

Note: the pinger runs in each running process as a daemon thread; this means that if your deployment has multiple workers or instances, each one will perform the ping and you'll see multiple requests every interval.

If you want exactly one ping per interval (recommended to avoid duplicate requests):
- Use Render cron jobs (recommended): create a job that calls your service URL every 14 minutes and set `PING_ENABLED=False` in the service env vars.
- Use an external uptime monitor (UptimeRobot, Cron-job.org, etc.) and set `PING_ENABLED=False` in env vars.
- If you prefer an in-app single-pinger, implement a distributed lock (Redis cache or Postgres advisory lock) so only one process performs the ping; this repository does not enable that by default.

To disable the internal pinger in Render when using an external cron/monitor, set:
```
PING_ENABLED=False
```

Troubleshooting tips:
- If `collectstatic` fails, ensure `STATIC_ROOT` is writable and `STATICFILES_STORAGE` is set (we use WhiteNoise storage).
- Check the build logs for missing packages and ensure `requirements.txt` is up to date.
