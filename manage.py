#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    
    try:
        # Import the execute_from_command_line function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError if Django is not available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute administrative tasks from the command line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Entry point for running administrative tasks
    main()
