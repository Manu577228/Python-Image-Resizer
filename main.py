import cv2

src = cv2.imread("virat.jpeg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src)

# percent by which the image is resized
scale_percent = 50

# calculate the 50% of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

#dsize
dsize = (width, height)

#resize image
output = cv2.resize(src, dsize)

cv2.imwrite('D:/cv2-resize-image-50.png', output)
cv2.waitKey(0)