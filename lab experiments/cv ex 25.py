
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
import os

# Create file selection window
root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

if not filename:
    print("No image selected.")
else:
    # Read the selected image
    image = cv2.imread(filename)

    if image is None:
        print("Error: Cannot open the image.")
    else:
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get the OpenCV Haar cascade file path
        cascade_path = os.path.join(
            cv2.data.haarcascades,
            "haarcascade_eye_tree_eyeglasses.xml"
        )

        # Load the detector
        detector = cv2.CascadeClassifier(cascade_path)

        if detector.empty():
            print("Error: Eye detector could not be loaded.")
        else:
            # Detect eye regions
            eyes = detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(25, 25)
            )

            # Draw rectangles around detected regions
            if len(eyes) > 0:
                print("Possible eye regions detected.")

                for (x, y, w, h) in eyes:
                    cv2.rectangle(
                        image,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )
            else:
                print("No eye regions detected.")

            # Display output
            image_rgb = cv2.cvtColor(
                image, cv2.COLOR_BGR2RGB
            )

            plt.imshow(image_rgb)
            plt.title("Spectacles / Eye Region Detection")
            plt.axis("off")
            plt.show()

root.destroy()
