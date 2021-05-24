import cv2
import numpy as np
import matplotlib.pyplot as mat_plt

image = cv2.imread('./assets/image.jpeg')
mat_plt.figure()
mat_plt.imshow(image, vmin=0, vmax=255, cmap=mat_plt.get_cmap('Greys'))
mat_plt.title('Original image')

image = cv2.imread('./assets/image.jpeg', cv2.IMREAD_GRAYSCALE)
image = 255 - image
height, width = image.shape
# Сжатие в 2 раза
image = cv2.resize(image, (width // 2, height // 2))

height, width = image.shape

dither_image = np.column_stack((image, [0] * image.shape[0]))
dither_image = \
    np.append(dither_image, [np.zeros(width + 1, dtype=np.uint8)], axis=0)
dither_image = dither_image.astype(np.float)

for h in range(height):
    for w in range(width):
        old_pixel = dither_image[h, w]
        # Лимит
        new_pixel = 255 if dither_image[h, w] > 96 else 0

        dither_image[h, w] = new_pixel

        err = old_pixel - new_pixel

        if w > 0:
            dither_image[h + 1, w - 1] = dither_image[
                                           h + 1, w - 1] + err * 3 / 16
        dither_image[h + 1, w] = dither_image[h + 1, w] + err * 5 / 16
        dither_image[h, w + 1] = dither_image[h, w + 1] + err * 7 / 16
        dither_image[h + 1, w + 1] = dither_image[h + 1, w + 1] + err * 1 / 16

dither_image = dither_image.astype(np.uint8)
dither_image = dither_image[0:height, 0:width]

mat_plt.figure()
mat_plt.imshow(dither_image, vmin=0, vmax=255, cmap=mat_plt.get_cmap('Greys'))
mat_plt.title('Dither')

mat_plt.show()
