from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera import PiCamera
import imutils
import time
import cv2
import numpy as np


time.sleep(2.0)
print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0) #to warm up the camera
fps = FPS().start()

#while fps._numFrames < 1000:(for testing)
while True:
        
	frame = vs.read()
	
	##########video processing/sending the frames to driver station############
	#(b,g,r) = frame[100,100]
	#print((b,g,r))
	#print(len(frame)) ################ just testing ###################
	
	fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

vs.stop()
