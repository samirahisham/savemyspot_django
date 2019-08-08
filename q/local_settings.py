
ALLOWED_HOSTS = ['127.0.0.1', '104.248.138.63', 'savemyspot-django.codeunicorn.io']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'be44006884456b6e63f99ed86358d1df',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
	"https://savemyspot-django.codeunicorn.io"
]