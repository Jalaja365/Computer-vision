
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

image = cv2.imread(filename)

if image is None:
    print("Image not selected or cannot be opened")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter in X direction
    sobel_x = cv2.Sobel(
        gray, cv2.CV_64F, 1, 0, ksize=3
    )

    # Apply Sobel filter in Y direction
    sobel_y = cv2.Sobel(
        gray, cv2.CV_64F, 0, 1, ksize=3
    )

    # Convert results to absolute values
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine both directions
    sobel = cv2.addWeighted(
        sobel_x, 0.5, sobel_y, 0.5, 0
    )

    # Display output
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(sobel_x, cmap="gray")
    plt.title("Sobel X")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(sobel_y, cmap="gray")
    plt.title("Sobel Y")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(sobel, cmap="gray")
    plt.title("Sobel Edge Detection")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

root.destroy()
