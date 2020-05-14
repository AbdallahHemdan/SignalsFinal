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


# Step 1
inputImage = cv2.imread('./image1.bmp')

row = inputImage.shape[0]
col = inputImage.shape[1]
m = int(input('Enter the value of m between [1 - 4] : '))

cv2.imshow("Input Image", inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
