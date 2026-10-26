
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
    height, width = image.shape[:2]

    # Select a central region of interest (ROI)
    x1 = width // 4
    y1 = height // 4
    x2 = 3 * width // 4
    y2 = 3 * height // 4

    # Crop the ROI
    roi = image[y1:y2, x1:x2].copy()

    # Copy the original image
    result = image.copy()

    # Paste the ROI at the top-left corner
    roi_h, roi_w = roi.shape[:2]
    result[0:roi_h, 0:roi_w] = roi

    # Convert BGR to RGB for display
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cropped = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    pasted = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cropped)
    plt.title("Cropped ROI")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(pasted)
    plt.title("ROI Pasted Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    cv2.imwrite("cropped_roi.png", roi)
    cv2.imwrite("pasted_roi.png", result)

    print("ROI cropped, copied and pasted successfully!")

root.destroy()
