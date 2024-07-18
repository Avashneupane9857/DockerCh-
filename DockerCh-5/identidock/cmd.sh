#!/bin/sh
set -e
if [ "$ENV" = "DEV" ]; then
    echo "this is development server"
    exec python "identidock.py"
else
    echo "this is the production server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:9191
fi

