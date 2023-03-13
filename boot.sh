#!/bin/sh
#
source env/bin/activate
flask db migrate
flask db upgrade
exec gunicorn --workers 4 -b 0.0.0.0:5000 main:app
