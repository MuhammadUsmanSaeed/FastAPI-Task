#!/bin/bash

exec celery -A app.celery_app.celery beat