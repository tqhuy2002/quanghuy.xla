import numpy as np
from PIL import Image


def roberts_operator(image_array):
    height, width = image_array.shape
    result = np.zeros((height - 1, width - 1))

    kernel_x = np.array([[1, 0],
                         [0, -1]])

    kernel_y = np.array([[0, 1],
                         [-1, 0]])

    for i in range(height - 1):
        for j in range(width - 1):
            region = image_array[i:i + 2, j:j + 2]
            roberts_x = np.sum(region * kernel_x)
            roberts_y = np.sum(region * kernel_y)
            result[i, j] = np.sqrt(roberts_x ** 2 + roberts_y ** 2)

    return result


img = Image.open('input/roberts_operator.jpg').convert('L')
img_array = np.array(img, dtype=np.float32)

roberts_edges = roberts_operator(img_array)

roberts_edges_image = Image.fromarray(roberts_edges.astype(np.uint8))
roberts_edges_image.show()
