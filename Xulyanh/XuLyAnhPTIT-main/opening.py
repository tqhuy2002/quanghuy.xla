import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def erosion(image_array, kernel):
    rows, cols = image_array.shape
    erosion_result = np.zeros_like(image_array)
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            min_val = np.min(image_array[i - 2:i + 3, j - 2:j + 3] * kernel)
            erosion_result[i, j] = min_val
    return erosion_result


def dilation(image_array, kernel):
    rows, cols = image_array.shape
    dilation_result = np.zeros_like(image_array)
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            max_val = np.max(image_array[i - 2:i + 3, j - 2:j + 3] * kernel)
            dilation_result[i, j] = max_val
    return dilation_result


img = Image.open('input/opening.jpg').convert('L')
image_array = np.array(img)

kernel = np.ones((5, 5), np.uint8)

erosion_result = erosion(image_array, kernel)

opening_result = dilation(erosion_result, kernel)

plt.subplot(121), plt.imshow(image_array, cmap='gray'), plt.title('Ảnh gốc')
plt.subplot(122), plt.imshow(opening_result, cmap='gray'), plt.title('Ảnh sau opening')
plt.show()

plt.imsave('output/opening_result.jpg', opening_result, cmap='gray')
