import cv2 
from deepface import DeepFace
import pygame
import random
import tkinter as tk
from tkinter import filedialog

# ---------- INIT ----------
pygame.mixer.init()

emotion_songs = {
    "happy": ["music/happy.mp3"],
    "sad": ["music/sad.mp3"],
    "angry": ["music/angry.mp3"],
    "neutral": ["music/neutral.mp3"]
}

def play_music(emotion):
    pygame.mixer.music.stop()
    song = random.choice(emotion_songs[emotion])
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def map_emotion(emotion):
    if emotion == "happy":
        return "happy"
    elif emotion == "sad":
        return "sad"
    elif emotion == "angry":
        return "angry"
    else:
        return "neutral"

# ---------- CAMERA MODE ----------
def open_camera():
    cap = cv2.VideoCapture(0)
    current_emotion = None

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )

            emotion = result[0]['dominant_emotion']
            key = map_emotion(emotion)

            if key != current_emotion:
                current_emotion = key
                play_music(key)

            cv2.putText(
                frame,
                f"Emotion: {key}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
        except:
            pass

        cv2.imshow("Camera Mode - Emotion Music Player", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

# ---------- IMAGE UPLOAD MODE ----------
def upload_image():
    img_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if not img_path:
        return

    img = cv2.imread(img_path)

    result = DeepFace.analyze(
        img,
        actions=['emotion'],
        enforce_detection=False
    )

    emotion = result[0]['dominant_emotion']
    key = map_emotion(emotion)

    play_music(key)

    cv2.putText(
        img,
        f"Emotion: {key}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Image Mode - Emotion Music Player", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

# ---------- GUI ----------
root = tk.Tk()
root.title("Emotion Based Music Player")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(
    root,
    text="Emotion Based Music Player",
    font=("Arial", 16, "bold")
).pack(pady=20)

tk.Button(
    root,
    text="📷 Use Camera",
    font=("Arial", 14),
    width=20,
    command=open_camera
).pack(pady=10)

tk.Button(
    root,
    text="📂 Upload Image",
    font=("Arial", 14),
    width=20,
    command=upload_image
).pack(pady=10)

root.mainloop()
