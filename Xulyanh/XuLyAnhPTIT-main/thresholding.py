from PIL import Image

img = Image.open('input/thresholding_input.jpg').convert('L')


threshold_value = 75
thresholded_img = img.point(lambda p: 255 if p > threshold_value else 0, mode='1')


thresholded_img.show()
