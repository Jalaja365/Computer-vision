
import cv2
from tkinter import Tk, filedialog

# Select a video file
root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
)

root.destroy()

if not video_path:
    print("No video selected.")
else:
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video.")
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Read all video frames
        frames = []

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frames.append(frame)

        cap.release()

        if len(frames) == 0:
            print("No frames found in the video.")
        else:
            # Create output video
            output_path = "reverse_video.avi"

            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            out = cv2.VideoWriter(
                output_path, fourcc, fps, (width, height)
            )

            # Write frames in reverse order
            for frame in reversed(frames):
                out.write(frame)

            out.release()

            print("Reverse video created successfully!")
            print("Saved as:", output_path)

            # Play the reversed video
            reversed_cap = cv2.VideoCapture(output_path)

            while True:
                ret, frame = reversed_cap.read()

                if not ret:
                    break

                cv2.imshow("Reverse Video", frame)

                if cv2.waitKey(max(1, int(1000 / fps))) & 0xFF == ord("q"):
                    break

            reversed_cap.release()
            cv2.destroyAllWindows()
