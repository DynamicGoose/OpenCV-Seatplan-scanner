from email.mime import image
from venv import create
import cv2
from cv2 import SimpleBlobDetector
from cv2 import drawKeypoints
from cv2 import DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
from cv2 import SimpleBlobDetector_create
from cv2 import SimpleBlobDetector_Params
from cv2 import DRAW_MATCHES_FLAGS_DEFAULT
from cv2 import DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
from cv2 import DrawMatchesFlags_DRAW_RICH_KEYPOINTS
from cv2 import circle
from cv2 import LINE_AA
import numpy as np
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey

params = SimpleBlobDetector_Params()

params.minThreshold = 0
params.maxThreshold = 255
params.thresholdStep = 1
params.filterByArea = True
params.minArea = 150
params.minRepeatability = 1
params.filterByColor = False

img = imread("test.jpg",1)

detector = SimpleBlobDetector_create(params)

seats = detector.detect(img)

img_ws = img.copy()

for keyPoint in seats:
    blobCenter = (int(keyPoint.pt[0]),int(keyPoint.pt[1]))
    circle(img_ws, blobCenter, 7, (0,0,255), thickness = -1, lineType = LINE_AA)  

imshow("seats", img_ws)
waitKey(0)