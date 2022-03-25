from email.mime import image
from tkinter import Y
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
params.minArea = 1000
params.minRepeatability = 1
params.filterByColor = False

img = imread("test3.jpg",1)

detector = SimpleBlobDetector_create(params)

seats = detector.detect(img)

img_ws = img.copy()

for keyPoint in seats:
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    circle(img_ws, (x,y), 7, (0,0,255), thickness=4, lineType=LINE_AA)
    print("INSERT INTO Platz (PlanID, Stuhl, BereichID, X, Y, Bez1, Bez2, Bez3, Reflex, Xe, Ye, Sitzplatz, BestBuy, Sort, Jacket, Platz, Rotate) VALUES (138, 'Reihe 6 - Platz 1', 1, ", x,", ", y, ", 'Block A', 'Reihe 6', 'Platz 1', 0, 0, 0, 1, 0, 0, NULL, 0, 0);")

imshow("plan", img_ws)
waitKey(0)