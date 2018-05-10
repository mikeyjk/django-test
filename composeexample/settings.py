SECRET_KEY = 'abc'
ALLOWED_HOSTS = ['*']

# https://docs.djangoproject.com/en/dev/ref/databases/#mysql-notes
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
