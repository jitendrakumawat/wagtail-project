from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

# DEBUG = True

try:
    from .local import *
except ImportError:
    pass
