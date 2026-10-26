
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

    # Create a structuring element
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    # Apply dilation
    dilated = cv2.dilate(
        gray, kernel, iterations=1
    )

    # Display original and dilated images
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(dilated, cmap="gray")
    plt.title("Dilated Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save the dilated image
    cv2.imwrite("dilated_image.png", dilated)
    print("Dilation completed successfully!")

root.destroy()
