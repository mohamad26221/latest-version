from pathlib import Path
import environ
import os
from datetime import timedelta
env =  environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '.env')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fwe(0fok*j(-(i2fjg(=&3x1mkwl9v$&+owjfi#z9-0%dx(kw9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'account',
    'service',
    'channels',
    'guardian',
    'universitie',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'subject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'subject.wsgi.application'
ASGI_APPLICATION = 'subject.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGES = [
    ('ar', 'Arabic'),
    ('en', 'English'),
]



LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Damascus'

USE_I18N = True

USE_TZ = True

USE_L10N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = "C:/Users/Administrator/Desktop/Django-project/venv/subject/staticfiles/"

# STATICFILES_DIRS = [
#     r"C:\Users\Administrator\Desktop\Django-project\venv\subject\staticfiles",
# ]



MEDIA_URL = '/media/'
MEDIA_ROOT = 'C:/Users/Administrator/Desktop/Django-project/venv/subject/account/attachments/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#REST_Framework_for_login
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', 
    'guardian.backends.ObjectPermissionBackend',
)

AUTH_USER_MODEL = 'account.Customuser'
REST_FRAMEWORK={
    'EXCEPTION_HANDLER': 'account.serializers.custom_exception_handler',
    'NON_FIELD_ERRORS_KEY':'error',
        'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    )

}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'garethbale26221@gmail.com'  
EMAIL_HOST_PASSWORD = 'jdpc bhga anpw deah'  
DEFAULT_FROM_EMAIL = 'Tishreen@gmail.com'  


PUSHER_APP_ID = env('PUSHER_APP_ID')
PUSHER_KEY = env('PUSHER_KEY')
PUSHER_SECRET = env('PUSHER_SECRET')
PUSHER_CLUSTER = env('PUSHER_CLUSTER')
PUSHER_SSL = True
