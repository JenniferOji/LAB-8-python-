import cv2
import numpy as np
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


img = cv2.imread('ATU.jpg',)

# # Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# to control the amount of rows and columns 
nrows = 2
ncols = 1

# the images on top 
plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('Gray Scale'), plt.xticks([]), plt.yticks([])
plt.show()


plt.show() 
