from scipy.fft import dct
import numpy as np
import cv2


# Steps to follow

# 1. Read the image file ‘image1.bmp’. => Done
# 2. Extract and display each of its three color components. => Done
# 3. process each color component in blocks of 8×8 pixels.
# 4. Obtain 2D DCT of each block.
# 5. Retain only the top left square of the 2D DCT coefficients of size 𝑚 × 𝑚, The rest of coefficients are ignored.
# 6. Compare the size of the original and compressed images.
# 7. Decompress the image by applying inverse 2D DCT to each block. Display the image.


# Step 2
def getComponent(inputImage, no):
    # 1. no = 0 => red
    # 2. no = 1 => green
    # 3. no = 2 => blue
    cpy = inputImage.copy()
    for i in range(3):
        if(i != no):  # not need => Just make it zeros
            cpy[:, :, i] = 0
    return cpy


# Step 1
inputImage = cv2.imread('./image1.bmp')

row = inputImage.shape[0]
col = inputImage.shape[1]
m = int(input('Enter the value of m between [1 - 4] : '))

cv2.imshow("Input Image", inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Step 2
# Get Red Component
blueComponent = getComponent(inputImage, 2)
cv2.imshow("Red Component", blueComponent)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get Green Component
greenComponent = getComponent(inputImage, 1)
cv2.imshow("Green Component", greenComponent)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get Blue Component
redComponent = getComponent(inputImage, 0)
cv2.imshow("Blue Component", redComponent)
cv2.waitKey(0)
cv2.destroyAllWindows()
