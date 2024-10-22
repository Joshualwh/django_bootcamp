URLs and Views Overview:
  1) URLs = Where
    - Request pizza
  2) View = What
    - Makes the pizza
  3) URLs and View work in pairs.

Django Project Setup:
  1) python -m venv env
  2) source env/bin/activate
  3) (optional) pip install django
  4) django-admin startproject {projectName} .
  5) python manage.py runserver.

Adding URLs and Views:
  1) Django projects consists of:
    - One project.
    - One or more Django apps.
      - No specific rules on how to create apps or structure them.
      - Multiple apps to separate your concerns.
  2) View is a python function or class.

Dynamic URLs Overview: a Look at the Django Docs:
  1) Django runs through each URL pattern top to bottom, stops at the one that matches.
  2) Static URL:
    - path('about/', about),
  3) Dynamic URL:
    - path('about/<int:year>', about),

