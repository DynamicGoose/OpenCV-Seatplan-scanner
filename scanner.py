from ast import If
from email.mime import image
from multiprocessing.sharedctypes import SynchronizedString
import string
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
from cv2 import resize
from cv2 import INTER_LINEAR
from cv2 import addWeighted
from cv2 import convertScaleAbs
import numpy as np
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey

params1 = SimpleBlobDetector_Params()

params1.minThreshold = 0
params1.maxThreshold = 255
params1.thresholdStep = 1
params1.filterByArea = True
params1.minArea = 150
params1.minRepeatability = 1
params1.filterByColor = False

img = imread("test4.jpg",1)
imshow("original", img)

detector = SimpleBlobDetector_create(params1)
seats = detector.detect(img)

img_ws = img.copy()

for keyPoint in seats:
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    circle(img_ws, (x,y), 5, (0,0,255), thickness=4, lineType=LINE_AA)

imshow("plan", img_ws)

sum = 0
for keyPoint in seats:
    sum = sum + keyPoint.size
average = np.average(sum / len(seats))
print(average)

res_divisor = average / 15

params2 = SimpleBlobDetector_Params()

params2.minThreshold = 0
params2.maxThreshold = 255
params2.thresholdStep = 1
params2.filterByArea = True
params2.minArea = 100
params2.minRepeatability = 1
params2.filterByColor = False

detector = SimpleBlobDetector_create(params2)

height = int(img_ws.shape[0] / res_divisor)
width = int(img_ws.shape[1] / res_divisor)
points = (int(width), int(height))
img_rs = resize(img, points, interpolation= INTER_LINEAR)
seats = detector.detect(img_rs)

for keyPoint in seats:
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    circle(img_rs, (x,y), 5, (0,0,255), thickness=4, lineType=LINE_AA)
    print("INSERT INTO Platz (PlanID, Stuhl, BereichID, X, Y, Bez1, Bez2, Bez3, Reflex, Xe, Ye, Sitzplatz, BestBuy, Sort, Jacket, Platz, Rotate) VALUES (138, 'Reihe 6 - Platz 1', 1, ", x,", ", y, ", 'Block A', 'Reihe 6', 'Platz 1', 0, 0, 0, 1, 0, 0, NULL, 0, 0);")

imshow("plan_final", img_rs)
waitKey(0)