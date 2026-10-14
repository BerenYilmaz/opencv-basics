import cv2 as cv
import matplotlib.pyplot as plt


noisy_image = cv.imread("image3.jpeg")
noisy_image_rgb = cv.cvtColor(noisy_image, cv.COLOR_BGR2RGB)

bilateral_denoised_img = cv.bilateralFilter(noisy_image, 9, 75, 75)
bilateral_denoised_img_rgb = cv.cvtColor(bilateral_denoised_img, cv.COLOR_BGR2RGB)

plt.figure()
plt.subplot(131)
plt.title('Bilateral Image')
plt.imshow(bilateral_denoised_img_rgb)
plt.axis('off')

plt.show()
