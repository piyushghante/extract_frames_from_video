import cv2
import os

# Set the input video filename, output filename, and framerate
input_filename = '4.mp4'
output_filename = 'timelapse_slowed_down.mp4'
output_fps = 60

# Create a new directory to store the output JPEG images
output_folder = 'timelapse_frames_{}'.format(os.getpid())
os.makedirs(output_folder)

# Open the input video file
cap = cv2.VideoCapture(input_filename)
if not cap.isOpened():
    print('Error: Failed to open input video file')
    exit()

# Get the video dimensions and framerate
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create the video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, output_fps, (width, height))

# Loop through each frame in the input video
while cap.isOpened():
    # Read the next frame from the input video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save the color frame as a JPEG image in the output folder
    jpeg_filename = os.path.join(output_folder, 'frame_{}.jpg'.format(int(cap.get(cv2.CAP_PROP_POS_FRAMES))))
    cv2.imwrite(jpeg_filename, frame)
    
    # Write the color frame to the output video multiple times to slow down the playback speed
    for i in range(int(fps/output_fps)):
        out.write(frame)

# Release the input video file and the video writer object
cap.release()
out.release()
