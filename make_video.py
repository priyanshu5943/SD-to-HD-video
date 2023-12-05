
#make the video out of images


import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import PIL
import argparse

# Define a function to convert a sequence of images to a video
def images_to_video(image_folder, video_name, fps):
    # Get a list of image files in the specified folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

    # Check if there are no images in the folder
    
    # Read the first image to get dimensions
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Create a VideoWriter object to write the video
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Sort the images based on the index in their filenames
    sorted_images = sorted(images, key=lambda x: int(x.split('_')[1].split('.')[0]))

    # Iterate through sorted images and write each frame to the video
    for image in sorted_images:
        img_path = os.path.join(image_folder, image)
        if os.path.isfile(img_path):
            video.write(cv2.imread(img_path))
        else:
            # Print a warning if an image is not found
            print(f"Warning: Image {image} not found.")

    # Release the VideoWriter to close the output video file
    video.release()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert a sequence of images to a video.")
    parser.add_argument("image_sequence_path", help="Path to the folder containing image sequence")
    parser.add_argument("file_path", help="Path to the video file for capture")
    parser.add_argument("output_video_name", help="Name of the output video file")
    args = parser.parse_args()

    # capture the video
    cap = cv2.VideoCapture(args.file_path)

    # check if capture was successful
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    fps = cap.get(cv2.CAP_PROP_FPS)

    # Example usage
    images_to_video(args.image_sequence_path, args.output_video_name, fps)