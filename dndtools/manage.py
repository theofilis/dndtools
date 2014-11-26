#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dndproject.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    from django.db import connection
    connection.connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")

