#!/usr/bin/env python
import os
import sys
import settings

"""
 使用环境变量RUN_WEB, 是基于python manage.py runserver autoreload机制
 python manage.py runserver 实际会触发两次
"""
def init(params):
    web = 'RUN_WEB' in os.environ.keys() and os.environ['RUN_WEB']
    if not web:
        for param in params:
            if param in settings.WEBS.keys():
                web = param
                params.remove(param)
                break
        if not web:
            web = settings.DEFAULT_WEB

        if not os.path.exists(web):
            raise ImportError("'WEB' or DEFAULT_WEB must be set correctly!")

        if 'runserver' in params and settings.WEBS[web]:
            params.append(settings.WEBS[web])

        os.environ['RUN_WEB'] = web

    setting_path = "%s.settings" % web
    return setting_path, params

if __name__ == "__main__":
    setting_path, params = init(sys.argv)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting_path)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
