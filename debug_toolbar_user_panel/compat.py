# Django 1.5 add support for custom auth user model
if django.VERSION >= (1, 5):
    from django.conf import settings
    if hasattr(settings, 'AUTH_USER_MODEL'):
        User = settings.AUTH_USER_MODEL
    else:
        from django.contrib.auth.models import User
else:
    try:
        from django.contrib.auth.models import User
    except ImportError:
        raise ImportError(u'User model is not to be found.')
