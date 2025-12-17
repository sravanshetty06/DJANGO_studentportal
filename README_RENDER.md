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

Troubleshooting tips:
- If `collectstatic` fails, ensure `STATIC_ROOT` is writable and `STATICFILES_STORAGE` is set (we use WhiteNoise storage).
- Check the build logs for missing packages and ensure `requirements.txt` is up to date.
