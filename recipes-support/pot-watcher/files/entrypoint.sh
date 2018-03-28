#!/bin/bash

if [ ! -e /usr/lib64/python3.5/site-packages/imutils ]; then
    pip3 install imutils
fi

# Make the video device available
# Cheat to get the device available in the container
# You can test with /root/cap.py
if [ ! -e /dev/video0 ]; then
    mknod /dev/video0 c 81 0
    sync
fi

# Start watching the pot
/usr/bin/python3 /root/pot-watcher.py 2>&1 > /tmp/out.log
