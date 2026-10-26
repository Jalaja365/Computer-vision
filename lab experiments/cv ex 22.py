
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

    # Apply closing operation
    closing = cv2.morphologyEx(
        gray, cv2.MORPH_CLOSE, kernel
    )

    # Display original and closed images
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(closing, cmap="gray")
    plt.title("Closing Operation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save the result
    cv2.imwrite("closing_image.png", closing)
    print("Closing operation completed successfully!")

root.destroy()
