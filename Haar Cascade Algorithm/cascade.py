# Import libraries
import cv2
import numpy as np

image = cv2.imread("images/test1.jpeg")
# image = image.resize((1000, 667))
image_arr = np.array(image)   # Converting the image to a numpy array

grey = cv2.cvtColor(image_arr, cv2.COLOR_RGB2GRAY)

blur = cv2.GaussianBlur(grey, (5, 5), 0)

dilated = cv2.dilate(blur, np.ones((3, 3)))

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

car_cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(car_cascade_src)
cars = car_cascade.detectMultiScale(image_arr, 1.1, 1)

cnt = 0
for (x, y, w, h) in cars:
    cv2.rectangle(image_arr, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cnt += 1
print("Vehicle Count: ", cnt)

cv2.imshow("Lane1", image_arr)
cv2.waitKey(0)
