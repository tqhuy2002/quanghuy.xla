import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Đọc ảnh
img = Image.open('input/erosion.jpg').convert('L')

image_array = np.array(img)

kernel = np.ones((5, 5), np.uint8)

rows, cols = image_array.shape

erosion_result = np.zeros_like(image_array)

for i in range(2, rows - 2):
    for j in range(2, cols - 2):
        # Áp dụng kernel và thực hiện erosion
        min_val = np.min(image_array[i - 2:i + 3, j - 2:j + 3] * kernel)
        erosion_result[i, j] = min_val

plt.subplot(121), plt.imshow(image_array, cmap='gray'), plt.title('Ảnh gốc')
plt.subplot(122), plt.imshow(erosion_result, cmap='gray'), plt.title('Ảnh sau erosion')
plt.show()

plt.imsave('output/erosion_result.jpg', erosion_result, cmap='gray')
