
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
    # Rotate image 90 degrees clockwise
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Convert images from BGR to RGB
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rotated = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(rotated)
    plt.title("90 Degree Clockwise Rotation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

root.destroy()
