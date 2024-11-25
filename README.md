# Home Library ( It is under development!!! ) 

"Home Library" website written in Django.

## Useful links

[The twelve-factor app](https://12factor.net/)

## Overview

This web application creates an online catalog for a home library, where users can browse available books and manage their accounts.

## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://github.com/EvilPencil/home-library/blob/master/server-set-up.md).
   We recommend using a Python virtual environment.
   > **Note:** This has been tested against Django 4.2 (and may not work or be "optimal" for other versions).
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
