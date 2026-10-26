
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

image = cv2.imread(filename)

if image is None:
    print("Image not selected or cannot be opened")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a kernel
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    # Apply erosion
    eroded = cv2.erode(gray, kernel, iterations=1)

    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    # Display eroded image
    plt.subplot(1, 2, 2)
    plt.imshow(eroded, cmap="gray")
    plt.title("Eroded Image")
    plt.axis("off")

    plt.show()

root.destroy()
