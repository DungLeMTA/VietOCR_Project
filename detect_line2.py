import cv2
import numpy as np
import time

start = time.time()
image = cv2.imread('./test/rr_skew.jpg')
#cv2.imshow('orig',image)
#cv2.waitKey(0)

# các giá trị remain , kernel phụ thuộc vào height và width của ảnh
remain = 3
height_kernel = 1
width_kernel = 20
#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('binary',thresh)
cv2.waitKey(0)

#dilation
kernel = np.ones((height_kernel,width_kernel), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated',img_dilation)
cv2.waitKey(0)

#find contours
# im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = image[y:y+h, x:x+w]

    # show ROI
    # cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x-remain,y-remain),( x + w + remain, y + h +remain),(90,0,255),1)
    # cv2.waitKey(0)

end = time.time()
cv2.imwrite('result_detect.jpg',image)
print('Thời gian: %.3f giây'%(end-start))
cv2.imshow('marked areas',image)
cv2.waitKey(0)