import numpy as np
from PIL import Image

img = Image.open('input/negative_image_input.jpg')

img_array = np.array(img)
negative_img_array = 255 - img_array
negative_img = Image.fromarray(negative_img_array)

negative_img.show()
