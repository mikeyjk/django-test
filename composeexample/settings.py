SECRET_KEY = 'abc'
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASS': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
