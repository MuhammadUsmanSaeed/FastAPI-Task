#!/bin/bash

exec celery -A app.celery_app.celery worker --loglevel=info --pool=prefork --uid=nobody --gid=nogroup