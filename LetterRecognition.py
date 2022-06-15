import cv2
from PIL import Image 
import numpy
src = cv2.imread(r'Letters/A/A_0.png',cv2.IMREAD_UNCHANGED)
trans_mask = src[:,:,3] = 0
src[trans_mask] = [255,255,255,255]
image = cv2.cvtColor(src, cv2.COLOR_BGRA2BGR)
cv2.imshow("hello", image)
cv2.waitKey(0)
