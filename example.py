import cv2

img = cv2.imread('tiger.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image',img)

# hist = cv2.calcHist([img],[0],None,[256],[0,255])
# print(hist)

cv2.waitKey(0)
cv2.destroyAllWindows()