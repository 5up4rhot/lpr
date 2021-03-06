"""
Django settings for lpr_project project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9(&jvr7y!mn*xij*2i9t!*=c(fdh9sz&#kl(&3+2tw_f^p@7*l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: allowed hosts all now!
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # user apps
    'home_app.apps.HomeAppConfig',
    'principles_app.apps.PrinciplesAppConfig',
    'news_app.apps.NewsAppConfig',
    'people_app.apps.PeopleAppConfig',
    'departments_app.apps.DepartmentsAppConfig',
    'accounts_app.apps.AccountsAppConfig',
    # ckeditor
    'ckeditor',
    'ckeditor_uploader',
    # django-sass-processor
    'sass_processor',
    # django-cities-light
    'cities_light',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lpr_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'lpr_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'sass_processor.finders.CssFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # ckeditor files goes here after collectstic, so we need it before deployment

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'styling'),
]

SASS_PROCESSOR_ROOT = STATIC_ROOT #online compiled css and css.map goes here
SASS_PROCESSOR_AUTO_INCLUDE = False #we dont need any scss or css from static_root folder

# MEDIA FILES SETTINGS
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DJANGO-CITIES-LIGHT SETTINGS
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['ru', 'en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['RU']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3',
                                   'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT', ]

# CKEDITOR SETTINGS
CKEDITOR_UPLOAD_PATH = 'news/images/'
CKEDITOR_FILENAME_GENERATOR = 'news_app.utils.get_filename'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = False
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_BROWSE_SHOW_DIRS = True


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'styles', 'items': ['Format', ]},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste',
                                            'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'document', 'items': ['Source', ]},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Iframe']},
            {'name': 'tools', 'items': ['ShowBlocks', ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            # your extra plugins here
            'image2',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/news/profile'

# TESTING EMAIL PASSWORD RESET
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
