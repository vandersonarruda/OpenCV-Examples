import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
print(img.shape) # tamanhos da imagem e quantos canais

imgResize = cv2.resize(img, (200,200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)