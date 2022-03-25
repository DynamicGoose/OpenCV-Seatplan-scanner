from ast import If
from email.mime import image
from multiprocessing.sharedctypes import SynchronizedString
import string
from tkinter import W, Y
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
from cv2 import add
from cv2 import INTER_NEAREST
from cv2 import INTER_LANCZOS4
from cv2 import INTER_LINEAR_EXACT
from cv2 import INTER_TAB_SIZE2
from cv2 import INTER_BITS
from cv2 import INTER_CUBIC
import numpy as np
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey

params = SimpleBlobDetector_Params()

params.minThreshold = 0
params.maxThreshold = 255
params.thresholdStep = 10
params.filterByArea = True
params.minArea = 150
params.minRepeatability = 1
params.filterByColor = False
params.filterByCircularity = False
params.filterByConvexity = True
params.minConvexity = 0.9
params.filterByInertia = True

gap = 100
minearea2 = 150

img = imread("test.jpg",1)

detector = SimpleBlobDetector_create(params)
seats = detector.detect(img)

img_ws = img.copy()

for keyPoint in seats:
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    circle(img_ws, (x,y), 7, (0,0,255), thickness=2, lineType=LINE_AA)

sum = 0
for keyPoint in seats:
    sum = sum + keyPoint.size
average = sum / len(seats)

res_divisor = average / 15

params.minArea = minearea2

detector = SimpleBlobDetector_create(params)

height = int(img_ws.shape[0] / res_divisor + gap)
width = int(img_ws.shape[1] / res_divisor + gap)
points = (int(width), int(height))
img_rs = resize(img, points, interpolation= INTER_LANCZOS4)
seats = detector.detect(img_rs)

f = open("D:\seatScanner\output.txt", "w")

for keyPoint in seats:
    x = int(keyPoint.pt[0])
    y = int(keyPoint.pt[1])
    circle(img_rs, (x,y), 7, (0,0,255), thickness=1, lineType=LINE_AA)
    f.write("INSERT INTO Platz (PlanID, Stuhl, BereichID, X, Y, Bez1, Bez2, Bez3, Reflex, Xe, Ye, Sitzplatz, BestBuy, Sort, Jacket, Platz, Rotate) VALUES (138, 'Reihe 6 - Platz 1', 1, ")
    f.write(str(x))
    f.write(", ")
    f.write(str(y))
    f.write(", 'Block A', 'Reihe 6', 'Platz 1', 0, 0, 0, 1, 0, 0, NULL, 0, 0);\n")

f.close()

imshow("original", img)
imshow("iteration_1", img_ws)
imshow("iteration_2", img_rs)
waitKey(0)