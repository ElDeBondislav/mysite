import os.path

import requests
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8f*at4)3byw#*q4fz31%v2*gp6vv#qr95y7yhjnybt4f(a!d_='

DEBUG = False
# '127.0.0.1',
ALLOWED_HOSTS = ['http://newtestshopcart.info/','newtestshopcart.info', 'http://www.newtestshopcart.info/',
                'https://newtestshopcart.info/', 'https://www.newtestshopcart.info/','https://testmysiteapptest.herokuapp.com/', 
                 '127.0.0.1']

INSTALLED_APPS = [
    'django_telegrambot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'django_user_agents',
    'mobiledetect'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mobiledetect.middleware.DetectMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# newloginapplciation.wsgi --log-file -
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_TELEGRAMBOT = {

    'MODE': 'WEBHOOK',

    'WEBHOOK_SITE': 'https://mywebsite.com',
    'WEBHOOK_PREFIX': '/tg',  # (Optional[str]) # If this value is specified,
    # a prefix is added to webhook url

    'STRICT_INIT': True,  # If set to True, the server will fail to start if some of the
    # apps contain telegrambot.py files that cannot be successfully
    # imported.

    'BOTS': [
        {
            'TOKEN': '5277046408:AAH_C8fFsOiTwI9In3aNYqB79Gy6-7Jf4ZE',

            #'ALLOWED_UPDATES':["message", "edited_channel_post", "callback_query"], # List the types of
            # updates you want your bot to receive. For example, specify
            # ``["message", "edited_channel_post", "callback_query"]`` to
            # only receive updates of these types. See ``telegram.Update``
            # for a complete list of available update types.
            # Specify an empty list to receive all updates regardless of type
            # (default). If not specified, the previous setting will be used.
            # Please note that this parameter doesn't affect updates created
            # before the call to the setWebhook, so unwanted updates may be
            # received for a short period of time.

            # 'TIMEOUT':(Optional[int|float]), # If this value is specified,
            # use it as the read timeout from the server

            # 'WEBHOOK_MAX_CONNECTIONS':(Optional[int]), # Maximum allowed number of
            # simultaneous HTTPS connections to the webhook for update
            # delivery, 1-100. Defaults to 40. Use lower values to limit the
            # load on your bot's server, and higher values to increase your
            # bot's throughput.

            # 'MESSAGEQUEUE_ENABLED':(Optinal[bool]), # Make this True if you want to use messagequeue

            # 'MESSAGEQUEUE_ALL_BURST_LIMIT':(Optional[int]), # If not provided 29 is the default value

            # 'MESSAGEQUEUE_ALL_TIME_LIMIT_MS':(Optional[int]), # If not provided 1024 is the default value

            # 'MESSAGEQUEUE_REQUEST_CON_POOL_SIZE':(Optional[int]), # If not provided 8 is the default value

            # 'POLL_INTERVAL' : (Optional[float]), # Time to wait between polling updates from Telegram in
            # seconds. Default is 0.0

            # 'POLL_CLEAN':(Optional[bool]), # Whether to clean any pending updates on Telegram servers before
            # actually starting to poll. Default is False.

            # 'POLL_BOOTSTRAP_RETRIES':(Optional[int]), # Whether the bootstrapping phase of the `Updater`
            # will retry on failures on the Telegram server.
            # |   < 0 - retry indefinitely
            # |     0 - no retries (default)
            # |   > 0 - retry up to X times

            # 'POLL_READ_LATENCY':(Optional[float|int]), # Grace time in seconds for receiving the reply from
            # server. Will be added to the `timeout` value and used as the read timeout from
            # server (Default: 2).
        },
        # Other bots here with same structure.
    ],

}
