import numpy as np
from PIL import Image


def histogram_equalization(image_array):
    histogram, _ = np.histogram(image_array.flatten(), bins=256, range=(0, 256))

    cdf = histogram.cumsum()

    cdf_masked = np.ma.masked_equal(cdf, 0)
    cdf_masked = (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
    cdf = np.ma.filled(cdf_masked, 0).astype('uint8')

    equalized_image = cdf[image_array]

    return equalized_image


img = Image.open('input/histogram_equalization.jpg').convert('L')
img_array = np.array(img)

equalized_img = histogram_equalization(img_array)

equalized_image = Image.fromarray(equalized_img)
equalized_image.show()
