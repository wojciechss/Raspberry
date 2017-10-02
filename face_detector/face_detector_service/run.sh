#!/bin/bash

gunicorn app:api --config gunicorn.conf
