#!/bin/sh
set -e
if [ "$ENV" = "DEV" ]; then
    echo "this is development server"
    exec python "identidock.py"
elif [ "$ENV" = 'UNIT' ]; then
    echo "Running Unit Tests"
    exec python "tests.py"
else
    echo "this is the production server"
    exec uwsgi --http 0.0.0.0:5002 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:9191
fi

