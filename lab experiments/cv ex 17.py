
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
    # Create a copy of the original image
    watermarked = image.copy()

    # Add watermark text
    text = "WATERMARK"

    cv2.putText(
        watermarked,
        text,
        (30, image.shape[0] - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    # Convert BGR to RGB for display
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB)

    # Display images
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.title("Watermarked Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save the watermarked image
    cv2.imwrite("watermarked_image.png", watermarked)
    print("Watermarked image saved successfully!")

root.destroy()
