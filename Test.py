from wsgiref.simple_server import make_server
import cv2
from cv2 import VideoCapture
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
#vid = cv2.VideoCapture(0)
#vid.set(cv2.CAP_PROP_FPS, 120)
#vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#while (True):
#    ret, frame = vid.read()
#    mask = cv2.inRange(frame,(125, 0, 0),(200, 200, 100))
#    target = cv2.bitwise_and(frame,frame, mask=mask)

 #   cv2.imshow('frame', target)

 #   if cv2.waitKey(1) == ord('q'):
  #      break
#
src = cv2.imread(r'Alphabet.png')
image1 = Image.open(r'Alphabet.png')
image1.resize([100,100])
image1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
mask2 = cv2.inRange(src, (0,0,0),(100,100,100))
target = cv2.bitwise_and(src,src, mask=mask2)

cv2.imshow("image1", image1)
cv2.imshow("image", mask2)
cv2.waitKey(0)

Label = tk.Label(image =image1)
Label.place(x=0,y=0)
Label.pack()




