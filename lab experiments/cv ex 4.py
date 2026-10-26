
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

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display original grayscale image
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    # Display equalized image
    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Histogram Equalized")
    plt.axis("off")

    plt.show()

root.destroy()
