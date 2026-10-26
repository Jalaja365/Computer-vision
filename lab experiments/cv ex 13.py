
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
    rows, cols = image.shape[:2]

    # Select three points from the original image
    points1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # Select their new positions
    points2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(points1, points2)

    # Apply affine transformation
    transformed = cv2.warpAffine(image, matrix, (cols, rows))

    # Convert BGR to RGB for display
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    transformed = cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(transformed)
    plt.title("Affine Transformed Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

root.destroy()
