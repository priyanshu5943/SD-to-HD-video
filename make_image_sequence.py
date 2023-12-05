# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C4jyypiFFpT8WgZTc5RKa11UEEoa5m4_
"""


import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import PIL
import argparse

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Process video file and extract frames')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the input video file')
    parser.add_argument('--output_dir', type=str, required=True, help='Path to the output directory')
    return parser.parse_args()

# Parse command-line arguments
args = parse_args()

# Create the output directory if it doesn't exist
output_dir = args.output_dir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Creating helper function

def load_img(filename, debug=False, norm=True, resize=None):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if norm:
        img = img / 255.
        img = img.astype(np.float32)
    if debug:
        print(img.shape, img.dtype, img.min(), img.max())

    if resize:
        img = cv2.resize(img, (resize[0], resize[1]))

    return img

def plot_all(images, axis='off', figsize=(16, 8)):

    fig = plt.figure(figsize=figsize, dpi=80)
    nplots = len(images)
    for i in range(nplots):
        plt.subplot(1, nplots, i + 1)
        plt.axis(axis)
        plt.imshow(images[i])
    plt.show()

# Open the video file
file_path = args.file_path
video_stream = cv2.VideoCapture(file_path)

# Get FPS of the video
fps = video_stream.get(cv2.CAP_PROP_FPS)

# Prepare to write frame filenames to a text file
frame_list_filename = os.path.join(output_dir, "frames_list.txt")
with open(frame_list_filename, 'w') as frame_list_file:
    # Read and save frames
    frame_idx = 0
    while video_stream.isOpened():
        ret, frame = video_stream.read()
        if not ret:
            break

        frame_filename = f"frame_{frame_idx}.jpg"
        full_frame_path = os.path.join(output_dir, frame_filename)
        cv2.imwrite(full_frame_path, frame)
        frame_list_file.write(frame_filename + '\n')

        frame_idx += 1

# Release the video stream
video_stream.release()
