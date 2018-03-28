#!/bin/bash

# We don't have a recipe for this
pip3 install imutils

# Cheat to get the device available in the container
# You can test with
# from imutils.video import VideoStream
# vs = VideoStream(resolution=(320, 240)).start()
# frame = vs.read()
# print(frame)
# vs.stop()
#
mknod /dev/video0 c 81 0
