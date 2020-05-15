from scipy.fft import dct ,idct
import numpy as np
import cv2


# Steps to follow

# 1. Encoder
#   1.1 Read the image file ‘image1.bmp’. => Done
#   1.2 Extract and display each of its three color components. => Done
#   1.3 Convert range of each component to [-128, 127] => Done
#   1.4 Form a matrix for the outImage with the new size => Done
#   1.5 Process each color component in blocks of 8×8 pixels. => Done
#   1.6 Obtain 2D DCT of each block. => Done
#   1.7 Retain only the top left square of the 2D DCT coefficients of size 𝑚 × 𝑚, The rest of coefficients are ignored. => Done
#   1.8 Compare the size of the original and compressed images. => Done

# 2. Decoder
#   2.1 load the out-image=>Done
#   2.2 display the compressed image=>Done
#   2.3 Form a matrix for the deCompressed image with the original size => Done
#   2.4 Get each block of to be decompressed.=>Done
#   2.5 apply inverse dct on each block=>Done
#   2.6 re-range the out image by adding 128 ranges from [0 : 255] => Done
#   2.7 display the decompressed image and Compare them => Done
#   2.8 quality of the decompressed image is measured using the Peak Signal-to-Noise Ratio PSNR)
#   2.9 technical report (advantages of using DCT instead of DFT)


# Step 1.3
def reRange(inputImage):
    print("inputImage before", inputImage)
    inputImage = inputImage.astype('int')
    inputImage -= 128
    print("inputImage after", inputImage)
    return inputImage

# Step 1.2
def getComponent(inputImage, no):
    # 1. no = 0 => red
    # 2. no = 1 => green
    # 3. no = 2 => blue
    cpy = inputImage.copy()
    for i in range(3):
        if(i != no):  # not need => Just make it zeros
            cpy[:, :, i] = 0
    return cpy



def imageCompression(inputImage, m, row, col):
    # Step 1.4
    outImage = np.zeros(
        (int((row / 8) * m), int((col / 8) * m), 3), dtype=np.float16)

    blockRow = int(row / 8)
    blockCol = int(col / 8)
    blockComponents = 3
    noIterations = 0

    # Step 1.5
    for x in range(0, blockRow):
        for y in range(0, blockCol):
            for z in range(0, blockComponents):
                noIterations += 1
                currentBlock = inputImage[x *
                                          8: x * 8 + 8, y * 8: y * 8 + 8, z]
                # Step 1.6, 1.7
                blockDCT = dct(dct(currentBlock.T, norm='ortho').T, norm='ortho')[0:m, 0:m]
                outImage[x * m: x * m + m, y * m: y * m + m, z] = blockDCT
    print("no Iterations", noIterations)
    print("outImage", outImage)
    return outImage


# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')
# step 2.6
def deReRange(deCopressedImage):

    deCopressedImage += 128
    deCopressedImage = deCopressedImage.astype('int')
    return deCopressedImage


def imageDeCompression(toBeCompressedImage ,m , row ,col):
    # Step 2.3
    deCompressedImage = np.zeros((int((row / m) * 8), int((col / m) * 8), 3), dtype=np.float16)

    blockRow = int(row / m)
    blockCol = int(col / m)
    blockComponents = 3
    noIterations = 0

    # Step 2.4
    for x in range(0, blockRow):
        for y in range(0, blockCol):
            for z in range(0, blockComponents):

                noIterations += 1
                currentBlock = toBeCompressedImage[x * m: x * m + m, y * m: y * m + m, z]
                deCompressedBlock = np.zeros((int(8), int(8)), dtype=np.float16)
                deCompressedBlock[0: m, 0: m] = currentBlock

                # Step 2.5
                blockIDCT = idct2(deCompressedBlock)
                deCompressedImage[x*8:x*8+8, y*8:y*8+8, z] = blockIDCT

     # Step 2.6
    deCompressedImage =deReRange(deCompressedImage)
    return deCompressedImage



# Step 1.1
inputImage = cv2.imread('./image1.bmp')
np.save("inputImage", inputImage)

row = inputImage.shape[0]
col = inputImage.shape[1]
m = int(input('Enter the value of m between [1 - 4] : '))

cv2.imshow("Input Image", inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Step 1.2
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

# Step 1.3
inputImage = reRange(inputImage)

# Step 1.8
outImage = imageCompression(inputImage, m, row, col)
print("Output Image", outImage)
np.save("outImage", outImage)

# Step 2.1
toBeCompressedImage = np.load("outImage.npy")

# Step 2.2
print("decompressed", toBeCompressedImage)
deRow = toBeCompressedImage.shape[0]
deCol = toBeCompressedImage.shape[1]

deCompressedImage = imageDeCompression(toBeCompressedImage, m, deRow, deCol)
print("deCompressedImage", deCompressedImage)
print("inputImage", inputImage)
print(deCompressedImage.shape[0], deCompressedImage.shape[1])

# Step 2.7
cv2.imwrite("deCompressedImage.png", deCompressedImage)
deCompressedImage = cv2.imread("./deCompressedImage.png")
cv2.imshow("deCompressed Image", deCompressedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

