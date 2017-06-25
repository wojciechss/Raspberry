#!/bin/bash

gunicorn app:api --config gunicorn.conf --timeout 3600
