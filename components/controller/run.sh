#!/bin/bash

gunicorn controller.app:api --config gunicorn.conf
