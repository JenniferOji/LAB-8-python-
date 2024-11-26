import cv2
import numpy as np
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


img = cv2.imread('ATU.jpg',)

# # Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# to control the amount of rows and columns 
nrows = 2
ncols = 3

# the images on top normal and grayscale
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('Gray Scale'), plt.xticks([]), plt.yticks([])

#adding the blur 
imgOut = cv2.GaussianBlur(gray_image,(3, 3),0)

# sobel x
sobelHorizontal = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=5) # x dir
plt.subplot(nrows, ncols,3),plt.imshow(sobelHorizontal, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

# sobel y
sobelVertical = cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=5) # y dir
plt.subplot(nrows, ncols,4),plt.imshow(sobelVertical, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# sobel x and y
sobelSum = sobelHorizontal + sobelVertical
plt.subplot(nrows, ncols,5),plt.imshow(sobelSum, cmap = 'gray')
plt.title('Sobel Sum'), plt.xticks([]), plt.yticks([])


# cann edge detection 
canny = cv2.Canny(gray_image,100,250)
plt.subplot(nrows, ncols,6),plt.imshow(canny, cmap = 'gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show() 
