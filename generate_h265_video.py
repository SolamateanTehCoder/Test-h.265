import cv2
import numpy as np

# Video parameters
width, height = 320, 240
fps = 30
duration = 10

# Calculate total number of frames
total_frames = fps * duration

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('random_video.h265', fourcc, fps, (width, height))

for _ in range(total_frames):
    # Generate a random frame
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    video_writer.write(frame)

video_writer.release()
print('Video created: random_video.h265')
