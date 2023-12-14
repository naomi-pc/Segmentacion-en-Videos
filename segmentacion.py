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

    total_pixeles = frame_diff.size
    porcentaje_cambio = (pixeles_cambiados / total_pixeles) * 100

    print(f'Porcentaje de cambio: {porcentaje_cambio:.2f}%')

    kernel = np.ones((2, 2), np.uint8)
    erodeImage = cv2.erode(binFrame, kernel, iterations = 1)
    if (porcentaje_cambio > 0.1):
      cv2.imshow('frame diff ',erodeImage)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

    prevImage = currentImage.copy()
    success,currentImage = vidcap.read()

  idRutas +=1