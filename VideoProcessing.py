import os
import numpy as np
import cv2




class VideoProcessing:
    def videoprocess():
        # Load the video
        cap = cv2.VideoCapture(
            r"C:\Users\manop\OneDrive\Pictures\Video Projects\Adipurush (Official Teaser) Telugu _ Prabhas _ Kriti Sanon _ Saif Ali Khan _ Om Raut _ Bhushan Kumar - Copy.mp4")
        # Initialise the empty frames llist
        frames = []
        # Reading the frames
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
            print('Frame added, total frames:', len(frames))
        cap.release()
        # Processinng the frames
        processsed_frames = []
        for frame in frames:
            # Convert into grey scale images
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # resizeing each  frames into 64 x64
            resized_frame = cv2.resize(gray_frame, (64, 64))
            # Appending the resized frames into processed_frames
            processsed_frames.append(resized_frame)
        # converting the processed into numpy array
        data = np.array(processsed_frames)
        return data



