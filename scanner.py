from email.mime import image
from venv import create
import cv2
from cv2 import SimpleBlobDetector
from cv2 import drawKeypoints
from cv2 import DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
from cv2 import SimpleBlobDetector_create
from cv2 import SimpleBlobDetector_Params
import numpy as np
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey

params = SimpleBlobDetector_Params()

params.minThreshold = 0
params.maxThreshold = 255
params.filterByArea = True
params.minArea = 100
params.minRepeatability = 1

img = imread("test.jpg",1)

detector = SimpleBlobDetector_create(params)

seats = detector.detect(img)

img_ws = drawKeypoints(img, seats, np.array([]), (0,0,255), DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

imshow("seats", img_ws)
waitKey(0)