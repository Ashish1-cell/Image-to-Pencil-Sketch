import cv2
img_location = 'C:/Users/ASHISH/Desktop/'
filename = input("Enter the file name:")
img = cv2.imread(img_location+filename)
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#invert the image
inverted_gray_image = 255 - gray_image
#blur the image
blurred_img = cv2.GaussianBlur(inverted_gray_image,(21,21),0)
#invert the blurred image
invert_blurred_img = 255 - blurred_img
#create pencil sketch image
pencil_sketch_img = cv2.divide(gray_image,invert_blurred_img,scale= 256.0)
cv2.imshow('Original Image', img)
cv2.imshow('New Image',pencil_sketch_img )
cv2.waitKey(0)

