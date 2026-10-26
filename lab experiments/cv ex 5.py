
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Function to analyze color histogram
def analyze_histogram(image):
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    plt.figure(figsize=(10, 5))

    for i, (color, name) in enumerate(
        zip(colors, channel_names)
    ):
        histogram = cv2.calcHist(
            [image], [i], None, [256], [0, 256]
        )

        plt.plot(histogram, color=color, label=name)

    plt.title("Color-Level Histogram")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.grid()
    plt.show()


# Select an image
root = Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

root.destroy()

if filename:
    image = cv2.imread(filename)

    if image is not None:
        # Display original image
        cv2.imshow("Original Image", image)

        # Analyze color levels
        analyze_histogram(image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Color histogram analysis completed!")
    else:
        print("Error: Unable to read image.")
else:
    print("No image selected.")

