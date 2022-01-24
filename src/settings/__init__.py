from decouple import config

if config('SETTINGS_CONFIGURATION', default=None) in [None, "local"]:
    from .local import *  # NOQA
else:
    from .base import *  # NOQA
