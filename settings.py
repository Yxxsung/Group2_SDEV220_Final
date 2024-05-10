INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticgiles',
    'cart'
]

#Static Files (CSS, Javascript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
#Meida files (upload user files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"