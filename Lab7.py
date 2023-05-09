import cv2

image = cv2.imread('redbull.jpg')
b,gr,r=cv2.split(image)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", gr)
cv2.imshow("Red Channel", r)
cv2.waitKey(0)
gr[:,:] = 0
image1 = cv2.merge([b, gr, r])
cv2.imshow('Last image', image1)
cv2.waitKey(0)