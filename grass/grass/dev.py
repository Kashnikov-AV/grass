# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6_-e4#0$hr1exfn6-v*fb_x@u#+oq2%^8wn-emk=y^tzi-pvt$'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
