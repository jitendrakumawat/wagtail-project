from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# For production comment top line and uncomment below two line
DEBUG = True
# ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-1h*j(onq4o)o1k!&b&n8jfi+@on73@2$*^jesd(wu^nxx18c)'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
