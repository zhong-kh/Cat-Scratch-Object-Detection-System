import random
import time
import os
import pygame
import cv2
from ultralytics import YOLO

model_path = "weight"
music_folder = "musics"
video_name_root = 'cat_video'
model = YOLO(model_path)

pygame.mixer.init()

music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3') or f.endswith('.wav')]

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0)

def record_video(duration=5, video_filename="cat_video"):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)

        if time.time() - start_time > duration:
            break

    out.release()
    print(f"Video saved as {video_filename}")


def play_music():
    if music_files:
        music_file = os.path.join(music_folder, music_files[random.randint(0, len(music_files))])
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        print(f"Playing music: {music_file}")
        while pygame.mixer.music.get_busy():
            pass
    else:
        print("No music files found.")



def detect_cat_grabbing():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for r in results:
            bs = r.boxes
            for b in bs:
                if 0 == b.cls and 0.7 <= b.conf:
                    print("Cat scratching detected! Playing music...")
                    play_music()
                    record_video(duration=5, video_filename=f"{video_name_root}_{int(time.time())}.avi")
                    break

        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


detect_cat_grabbing()