
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

# Select an image
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

    # Create a morphological kernel
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    # Apply Black-Hat operation
    blackhat = cv2.morphologyEx(
        gray, cv2.MORPH_BLACKHAT, kernel
    )

    # Display original and Black-Hat images
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(blackhat, cmap="gray")
    plt.title("Black-Hat Operation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save the output image
    cv2.imwrite("blackhat_image.png", blackhat)
    print("Black-Hat operation completed successfully!")

root.destroy()
