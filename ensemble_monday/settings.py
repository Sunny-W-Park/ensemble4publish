"""AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'

Django settings for ensemble_monday project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '$^e7cfr2n_pob(de$fyc_zq9ij3=!p17jfjrsu=f!w_yu!#@(w')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )  #20/07/06 Django will display a standard 404 page

ALLOWED_HOSTS = ['localhost', 'http://192.168.0.8:8000', '192.168.0.8', '192.168.0.179', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    #'polls.apps.PollsConfig',
    'polls.apps.PollsConfig',
    'daemun.apps.DaemunConfig',
    'faq.apps.FaqConfig',
    'team.apps.TeamConfig',
    'imagekit',
    'crispy_forms',
    'hitcount',
    'gsheets',
    ]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ensemble_monday.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['ensemble_monday/templates/'],
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

WSGI_APPLICATION = 'ensemble_monday.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ensemble_monday',
        'USER': 'root',
        'PASSWORD': 'tjsdn8585!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )

#if DEBUG:
#    STATICFILES_DIRS = [
#        os.path.join(BASE_DIR, 'static')
#    ]
#else:
#    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ADMINS
# When DEBUG=False and AminEmailHandler is configured in LOGGING(done by default), Django emails these people the details of exceptions raised in the request/response cycle.
# Must be added in the real project

#Login
LOGIN_URL = '/users/login/' #Login URL
LOGIN_REDIRECT_URL = '/users/main/' #Post-Login URL
LOGOUT_REDIRECT_URL = '/' #Post-Logout URL
AUTH_USER_MODEL = "users.User" #Custom Auth Model

#Hitcount

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# django_heroku==0.3.1
import django_heroku
django_heroku.settings(locals())


# django_email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ensemble.kor@gmail.com'
EMAIL_HOST_PASSWORD = 'Ensemble123!'
SERVER_EMAIL = 'ensemble.kor@gmail.com'
DEFAULT_FROM_MAIL = 'ensemble.kor'




