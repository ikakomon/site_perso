#!/usr/bin/env python
import os
import sys
from decouple import config, Csv
if __name__ == "__main__":
    if config('DEBUG', default=False, cast=bool)==True:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
    else: 
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
