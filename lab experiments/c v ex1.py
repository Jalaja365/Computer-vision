import cv2
import matplotlib.pyplot as plt

image = cv2.imread("photo.jpg")

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.show()
