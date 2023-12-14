import cv2
import os
import numpy as np

rutas = ["videoSegmentation/vid1.mp4","videoSegmentation/vid2.mp4","videoSegmentation/vid3.mp4"]
idRutas = 1
for i in rutas:
    vidcap = cv2.VideoCapture(i)
    success,currentImage = vidcap.read()
    prevImage = currentImage
    print(idRutas)
    count = 0
