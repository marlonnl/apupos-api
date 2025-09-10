#!/usr/bin/env bash
mkdir -p media
python manage.py collectstatic --noinput
