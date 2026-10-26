
import cv2
from tkinter import filedialog
import tkinter as tk
import time

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[
        ("Video files", "*.mp4 *.avi *.mov *.mkv")
    ]
)

cap = cv2.VideoCapture(filename)

if not cap.isOpened():
    print("Video not selected or cannot be opened")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25

    print("Press 1 for Slow Motion")
    print("Press 2 for Fast Motion")
    print("Press 0 to Exit")

    mode = input("Enter your choice: ")

    if mode == "1":
        delay = int(1000 / (fps / 2))
    elif mode == "2":
        delay = int(1000 / (fps * 2))
    else:
        delay = int(1000 / fps)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video Processing", frame)

        if cv2.waitKey(max(1, delay)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

root.destroy()
