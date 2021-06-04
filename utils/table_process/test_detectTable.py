from DetectTable import DetectTable
import cv2

img = "B:\PycharmProjects\VietOCR_Project\img_2.png"
image = cv2.imread(img)
a = DetectTable(image)
cv2.imshow('',a.run(1))
cv2.waitKey()
