
import cv2
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt

# Select an image
root = Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

if not filename:
    print("No image selected.")
else:
    # Read the image
    image = cv2.imread(filename)

    if image is None:
        print("Error: Cannot open image.")
    else:
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Load the pretrained face detector
        cascade_path = (
            cv2.data.haarcascades
            + "haarcascade_frontalface_default.xml"
        )

        face_cascade = cv2.CascadeClassifier(cascade_path)

        if face_cascade.empty():
            print("Error: Face detector could not be loaded.")
        else:
            # Detect faces
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            print("Number of faces detected:", len(faces))

            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(
                    image,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

            # Display the result
            image_rgb = cv2.cvtColor(
                image, cv2.COLOR_BGR2RGB
            )

            plt.imshow(image_rgb)
            plt.title("Face Detection")
            plt.axis("off")
            plt.show()
