import cv2
import numpy as np

# * OBS: Zeros significa cor preta

img = np.zeros((512,512, 3), np.uint8)

# OBS: Código em BGR
# [:] -> imagem inteira
# img[:] = 255,0,0
# img[200:300,100:300] = 255,0,0

cv2.line(img,(0,0),(img.shape[1],300), (0,255,0),3)
cv2.rectangle(img, (0,0), (250,350),(0,0,255), 2)
# cv2.rectangle(img, (0,0), (250,350),(0,0,255), cv2.FILLED)
# Para preencher o quadrado, use FILLED no espessura
cv2.circle(img, (400,50), 30, (255,255,0), 5)
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image", img)

cv2.waitKey(0)