from settings import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.remove('south') if 'south' in INSTALLED_APPS else None
    INSTALLED_APPS.remove('tinymce') if 'tinymce' in INSTALLED_APPS else None
except Exception as e:
    pass
