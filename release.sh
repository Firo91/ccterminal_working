#!/bin/bash

cd equipment_log/
# Execute your command

python manage.py migrate
python manage.py makesuperuser