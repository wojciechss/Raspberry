#!/bin/bash

gunicorn app:api -b 127.0.0.1:5000 -b [::1]:5000 --keyfile server.key --certfile server.crt