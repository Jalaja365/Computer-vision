
import cv2
import numpy as np
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

    # Convert grayscale image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(
        gray, blockSize=2, ksize=3, k=0.04
    )

    # Dilate corner response for better visibility
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    result = image.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Convert images from BGR to RGB
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.title("Harris Corner Detection")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

root.destroy()
