from bichan.settings._base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DATABASE_NAME"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
        "HOST": "127.0.0.1",
        "PORT": os.environ["DATABASE_PORT"],
    }
}

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
