from scipy.fft import dct
import numpy as np
import cv2


# Steps to follow

# 1. Read the image file ‘image1.bmp’. => Done
# 2. Extract and display each of its three color components. => Done
# 3. Convert range of each component to [-128, 127] => Done
# 4. Form a matrix for the outImage with the new size => Done
# 5. Process each color component in blocks of 8×8 pixels. => Done
# 6. Obtain 2D DCT of each block. => Done
# 7. Retain only the top left square of the 2D DCT coefficients of size 𝑚 × 𝑚, The rest of coefficients are ignored. => Done
# 8. Compare the size of the original and compressed images. => Done
# 9. Decompress the image by applying inverse 2D DCT to each block. Display the image.


# Step 3
def reRange(inputImage):
    print("inputImage before", inputImage)
    inputImage = inputImage.astype('int')
    inputImage -= 128
    print("inputImage after", inputImage)
    return inputImage


def imageCompression(inputImage, m, row, col):
    # Step 4
    outImage = np.zeros(
        (int((row / 8) * m), int((col / 8) * m), 3), dtype=np.float16)

    blockRow = int(row / 8)
    blockCol = int(col / 8)
    blockComponents = 3
    noIterations = 0

    # Step 5
    for x in range(0, blockRow):
        for y in range(0, blockCol):
            for z in range(0, blockComponents):
                noIterations += 1
                currentBlock = inputImage[x *
                                          8: x * 8 + 8, y * 8: y * 8 + 8, z]
                # Step 6, 7
                blockDCT = dct(dct(currentBlock.T, norm='ortho').T,
                               norm='ortho')[0:m, 0:m]
                outImage[x * m: x * m + m, y * m: y * m + m, z] = blockDCT
    print("no Iterations", noIterations)
    print("outImage", outImage)
    return outImage


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
np.save("inputImage", inputImage)

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

# Step 3
inputImage = reRange(inputImage)

# Step 8
outImage = imageCompression(inputImage, m, row, col)
print("Output Image", outImage)
np.save("outImage", outImage)
