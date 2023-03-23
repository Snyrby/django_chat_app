#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# create home page
# crud
# search bar
# create with user authentication
# restrict pages if user is not logged in
# hide content if user is not logged in like edit page if it's not theirs
# prevent user from manually going to login page if they're logged in to prevent multiple login attempts.
# create registration page
# allow user to commend on pages
# user profile page
# link everything together
# static files on settings page
# install theme
# transfer files
# load static files for css
# transfer code into main and home page
# extend main page

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat_app.settings')
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
