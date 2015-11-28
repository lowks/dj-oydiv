from __future__ import absolute_import, unicode_literals
import os, sys

import django

from django.conf import settings


my_settings = dict(
    DEBUG=True,
    OYDIV_CRYPTO_KDF_ITERATIONS=1,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/testdb.sqlite3',
        }
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'dj_oydiv',
        'tests' # find our abstract models
    ],
    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware'
    ],
)


if __name__ == '__main__':
    settings.configure(**my_settings)
    try:
        django.setup()
    except AttributeError:
        # django < 1.7
        pass
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['tests', ])
    sys.exit(failures)
