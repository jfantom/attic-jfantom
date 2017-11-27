#!/bin/bash
gunicorn --bind 0.0.0.0:9999 -w 1 --worker-class gevent jfantom.main:app