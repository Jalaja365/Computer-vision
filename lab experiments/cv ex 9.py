
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
    # Resize to a bigger size
    bigger = cv2.resize(
        image, None, fx=2, fy=2,
        interpolation=cv2.INTER_LINEAR
    )

    # Resize to a smaller size
    smaller = cv2.resize(
        image, None, fx=0.5, fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Convert BGR to RGB for display
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    bigger = cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB)
    smaller = cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(bigger)
    plt.title("Bigger Image (2x)")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(smaller)
    plt.title("Smaller Image (0.5x)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

root.destroy()
