
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

    # Four points from the original image
    points1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Four points for the transformed image
    points2 = np.float32([
        [50, 50],
        [cols - 50, 0],
        [0, rows - 50],
        [cols - 1, rows - 1]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(points1, points2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(
        image, matrix, (cols, rows)
    )

    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    transformed = cv2.cvtColor(
        transformed, cv2.COLOR_BGR2RGB
    )

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(transformed)
    plt.title("Perspective Transformed")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

root.destroy()
