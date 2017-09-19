#!/bin/bash
exec gunicorn -w 5 -b 0.0.0.0:$PORT __init__:app     
