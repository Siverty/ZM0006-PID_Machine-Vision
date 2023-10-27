import cv2
import os
import numpy as np

# Set the path to the train folder
train_folder = "datasets/Labels_PID/images/train"
label_folder = "datasets/Labels_PID/labels/train"
save_folder = "datasets/Labels_PID/images/train"
save_label_folder = "datasets/Labels_PID/labels/train"

# Create the save folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Loop through each image in the folder
for filename in os.listdir(train_folder):
    # Check if the file name starts with "eroded_"
    if filename.startswith("eroded_"):
        print(f"{filename} already eroded, skipping...")
        continue

    # Load the image
    img = cv2.imread(os.path.join(train_folder, filename))

    # Define the kernel for filter2D
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

    # Apply filter2D to the image
    filtered = cv2.filter2D(img, -1, kernel)

    # Check if the filtered image already exists
    filtered_filename = os.path.join(save_folder, "filtered_" + filename)
    if os.path.exists(filtered_filename):
        print(f"{filtered_filename} already exists, skipping...")
        continue

    # Check if the filtered label file already exists
    label_filename = os.path.splitext(filename)[0] + ".txt"
    filtered_label_filename = os.path.join(save_label_folder, "filtered_" + label_filename)
    if os.path.exists(filtered_label_filename):
        print(f"{filtered_label_filename} already exists, skipping...")
        continue

    # Copy the label file and prepend the filename with "filtered_"
    with open(os.path.join(label_folder, label_filename), 'r') as f:
        label_content = f.read()
    with open(filtered_label_filename, 'w') as f:
        f.write(label_content)

    # Save the filtered image
    cv2.imwrite(os.path.join(save_folder, "filtered_" + filename), filtered)

    # Copy the label file and prepend the filename with "filtered_"
    label_filename = os.path.splitext(filename)[0] + ".txt"
    with open(os.path.join(label_folder, label_filename), 'r') as f:
        label_content = f.read()
    with open(os.path.join(save_label_folder, "filtered_" + label_filename), 'w') as f:
        f.write(label_content)
