import cv2
import os

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
    # Check if the file name starts with "blur_" or "blur_"
    if filename.startswith("eroded_"):
        os.remove(os.path.join(train_folder, filename))
        os.remove(os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt"))
        print(f"{filename} deleted...")
        continue

    elif filename.startswith("blur_"):
        print(f"{filename} already blurred, skipping...")
        continue

    # Load the image
    img = cv2.imread(os.path.join(train_folder, filename))

    # Define the kernel for erosion
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) # 5x5 kernel

    # Erode the image
    eroded = cv2.erode(img, kernel, iterations=1)

    # Check if the eroded image already exists
    eroded_filename = os.path.join(save_folder, "eroded_" + filename)
    if os.path.exists(eroded_filename):
        print(f"{eroded_filename} already exists, skipping...")
        continue

    # Check if the eroded label file already exists
    label_filename = os.path.splitext(filename)[0] + ".txt"
    eroded_label_filename = os.path.join(save_label_folder, "eroded_" + label_filename)
    if os.path.exists(eroded_label_filename):
        print(f"{eroded_label_filename} already exists, skipping...")
        continue

    # Copy the label file and prepend the filename with "eroded_"
    with open(os.path.join(label_folder, label_filename), 'r') as f:
        label_content = f.read()
    with open(eroded_label_filename, 'w') as f:
        f.write(label_content)

    # Save the eroded image
    cv2.imwrite(os.path.join(save_folder, "eroded_" + filename), eroded)

    # Copy the label file and prepend the filename with "eroded_"
    label_filename = os.path.splitext(filename)[0] + ".txt"
    with open(os.path.join(label_folder, label_filename), 'r') as f:
        label_content = f.read()
    with open(os.path.join(save_label_folder, "eroded_" + label_filename), 'w') as f:
        f.write(label_content)
