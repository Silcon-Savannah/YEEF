#!/bin/bash
set -e
set -o pipefail # if any code doesn't return 0, exit the script


function setup_server() {
  python server/manage.py makemigrations
  python server/manage.py migrate
  echo "from api.authentication.models import User; User.objects.filter(mobile_number='256788088831').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'password@yeef')" | python server/manage.py shell
  if [[ $ENVIRONMENT = "production" ]]; then
    python server/manage.py collectstatic --noinput
  fi
}

function start_server() {
  if [[ $ENVIRONMENT = "production" ]]; then
    echo Starting Gunicorn server..
    exec gunicorn a_socials.wsgi:application \
      --bind 0.0.0.0:8000 \
      --workers 3
  else
    echo Starting Django development server..
    python server/manage.py runserver 0.0.0.0:8000
  fi
}

setup_server
start_server

exit 0
