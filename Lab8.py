import cv2
import numpy as np
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


img = cv2.imread('ATU.jpg',)

# # Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# to control the amount of rows and columns 
nrows = 2
ncols = 2

# the images on top normal and grayscale
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('Gray Scale'), plt.xticks([]), plt.yticks([])

#adding the blur 
imgOut = cv2.GaussianBlur(gray_image,(3, 3),0)

# gray scale images on the bottom 
plt.subplot(nrows, ncols,3),plt.imshow(imgOut, cmap = 'gray')
plt.title('3 x 3'), plt.xticks([]), plt.yticks([])

# adding a blur 
imgOut2 = cv2.GaussianBlur(gray_image,(13, 13),0)

plt.subplot(nrows, ncols,4),plt.imshow(imgOut2, cmap = 'gray')
plt.title('13 x 13'), plt.xticks([]), plt.yticks([])

plt.show() 
