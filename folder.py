import os
import shutil

# Define the source folder and the target folders
source_folder = 'dumb_train_but_snippet'
target_folders = ['kiki-label', 'maxmax-label', 'juju-label']

# Ensure target folders exist
for folder in target_folders:
    os.makedirs(folder, exist_ok=True)

# List all the image files in the source folder
image_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Calculate the number of images per folder
num_images_per_folder = len(image_files) // len(target_folders)

# Distribute the images evenly among target folders
for i, folder in enumerate(target_folders):
    start_idx = i * num_images_per_folder
    end_idx = (i + 1) * num_images_per_folder if i < len(target_folders) - 1 else None

    for image_file in image_files[start_idx:end_idx]:
        source_path = os.path.join(source_folder, image_file)
        target_path = os.path.join(folder, image_file)
        shutil.copy(source_path, target_path)

print("Images distributed evenly among folders.")
