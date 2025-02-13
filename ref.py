import os
import ffmpeg
import cv2
from PIL import Image
import einops
from tqdm import tqdm

def video_to_pil_frames(video_path, output_dir):
    print(f"Fetching Frames: {video_path}")
    video = cv2.VideoCapture(video_path)
    os.makedirs(output_dir,exist_ok = True)
    
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total Frames: {total_frames}")

    for i in tqdm(range(total_frames), desc="Fetching Frames"):
        ret, frame = video.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        
        pil_image.save(f"{output_dir}/frame_{i}.png")
        # print(f"saved frame_{i}.png")
        # Yield one frame at a time


    video.release()
    
    print(f"save frames to {output_dir}")
    
video_path =  '/Users/mario/Downloads/Star Wars (1977).mp4'
output_dir = '/Users/mario/Desktop/ece910/output'

video_to_pil_frames(video_path, output_dir)