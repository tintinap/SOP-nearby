#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import py_eureka_client.eureka_client as eureka_client


def main():
    eureka_client.init(eureka_server="http://localhost:8761/eureka/",
                        app_name="SUGGEST-NEARBY-API",
                        instance_port=8989
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SOP.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
