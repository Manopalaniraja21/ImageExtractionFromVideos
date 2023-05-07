import cv2
import os

def extract_frames(video_path, output_dir):
    """Extract frames from a video and save them as image files."""
    video = cv2.VideoCapture(video_path)
    success, frame = video.read()
    count = 0
    while success:
        # Save the frame as an image file
        filename = os.path.join(output_dir, f'frame{count:06d}.jpg')
        cv2.imwrite(filename, frame)

        # Increment the frame count and read the next frame
        count += 1
        success, frame = video.read()
        print(count)
    video.release()

if __name__ == '__main__':
    video_path = r'C:\Users\manop\OneDrive\Pictures\Video Projects\Adipurush (Official Teaser) Telugu _ Prabhas _ Kriti Sanon _ Saif Ali Khan _ Om Raut _ Bhushan Kumar - Copy.mp4'
    output_dir = 'frames'
    os.makedirs(output_dir, exist_ok=True)
    extract_frames(video_path, output_dir)
