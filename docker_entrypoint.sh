#!/bin/sh
echo "Starting saap module..."
pre-commit install &
uvicorn app.main:app --host 0.0.0.0 --reload --proxy-headers --port 8000
