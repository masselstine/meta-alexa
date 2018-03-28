#!/bin/bash

cd /root
(ssh -N -R $SEER_ENDPOINT_PORT:localhost:5000 alexa@home.tundrafam.ca)&
/usr/bin/python overc-seer-hub.py
