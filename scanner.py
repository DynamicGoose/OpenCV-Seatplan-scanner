from email.mime import image
from venv import create
import cv2
from cv2 import SimpleBlobDetector
from cv2 import drawKeypoints
from cv2 import DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
from cv2 import SimpleBlobDetector_create
import numpy as np
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey

img_gs = imread("test.jpg",0)

detector = SimpleBlobDetector_create()

seats = detector.detect(img_gs)

img_ws = drawKeypoints(img_gs, seats, np.array([]), (0,0,255), DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

imshow("seats", img_ws)
waitKey(0)