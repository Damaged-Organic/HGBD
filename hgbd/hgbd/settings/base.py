# hgbd_project/hgbd/hgbd/settings/base.py
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'metadata.apps.MetadataConfig',
    'website.apps.WebsiteConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
]

ROOT_URLCONF = 'hgbd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'website/templates'),
        ],
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

WSGI_APPLICATION = 'hgbd.wsgi.application'

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':   'hgbd',
        'OPTIONS': {
            'use_unicode': True,
            'charset':     'utf8',
        }
    }
}

# Password validation

PASSWORD_VALIDATION = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': PASSWORD_VALIDATION + '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': PASSWORD_VALIDATION + '.MinimumLengthValidator',
    },
    {
        'NAME': PASSWORD_VALIDATION + '.CommonPasswordValidator',
    },
    {
        'NAME': PASSWORD_VALIDATION + '.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'uk'

LANGUAGES = (
    ('uk', 'UK'),
)

TRANSMETA_DEFAULT_LANGUAGE = 'uk'

SOLID_I18N_USE_REDIRECTS = False

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'website/locale'),
]

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Security

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Socials

SOCIALS = {
    'facebook': '',
}
