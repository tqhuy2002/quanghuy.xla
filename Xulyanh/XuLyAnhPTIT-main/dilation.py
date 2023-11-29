import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

img = Image.open('input/dilation.jpg').convert('L')

image_array = np.array(img)

kernel = np.ones((5, 5), np.uint8)

rows, cols = image_array.shape

dilation_result = np.zeros_like(image_array)

for i in range(2, rows - 2):
    for j in range(2, cols - 2):
        max_val = np.max(image_array[i - 2:i + 3, j - 2:j + 3] * kernel)
        dilation_result[i, j] = max_val

plt.subplot(121), plt.imshow(image_array, cmap='gray'), plt.title('Ảnh gốc')
plt.subplot(122), plt.imshow(dilation_result, cmap='gray'), plt.title('Ảnh sau dilation')
plt.show()

plt.imsave('output/dilation_result.jpg', dilation_result, cmap='gray')
