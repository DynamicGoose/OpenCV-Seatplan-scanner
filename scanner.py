from email.mime import image
import cv2
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey

img = imread("test.jpg",1)

imshow("image",img)

waitKey(0)