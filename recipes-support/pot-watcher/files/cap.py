# Capture a single image from the webcam
#
# usage: python3 cap.py > img.jpg
#
import cv2
import imutils
from imutils.video import VideoStream
import time, sys
vs = VideoStream(resolution=(320, 240)).start()
time.sleep(1.0)
while(True):
   #read frame by frame the webcame stream
   frame = vs.read()

   # encode as a JPEG
   res = bytearray(cv2.imencode(".jpeg", frame)[1])
   size = str(len(res))
   # stream to the stdout
   sys.stdout.write("Content-Type: image/jpeg\r\n")
   sys.stdout.write("Content-Length: " + size + "\r\n\r\n")
   sys.stdout.buffer.write( res )
   sys.stdout.write("\r\n")
   # we use 'informs' as a boundary   
   sys.stdout.write("--informs\r\n")
   break

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cv2.destroyAllWindows()
vs.stop()
