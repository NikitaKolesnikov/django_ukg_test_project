"""
Imports all base settings and overrides some of them to enhance local development.
"""
from .base import *  # NOQA

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testdjango.com', '0.0.0.0']
# SWAGGER_SETTINGS["VALIDATOR_URL"] = "http://0.0.0.0:8000"

# MIDDLEWARE.insert(7, "apps.utils.middleware.query_log_middleware")

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'django.db.backends': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
