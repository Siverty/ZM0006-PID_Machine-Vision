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
    if filename.startswith("blur_"):
        os.remove(os.path.join(train_folder, filename))
        os.remove(os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt"))
        print(f"{filename} deleted...")
        continue

    elif filename.startswith("eroded_"):
        print(f"{filename} already eroded, skipping...")
        continue

    # Load the image
    img = cv2.imread(os.path.join(train_folder, filename))

    # Define the kernel for erosion
    kernel = (9, 9) # 5x5 kernel for blurring

    # Blur the image
    blurd = cv2.GaussianBlur(img, kernel, 0)

    # Save the blured image
    cv2.imwrite(os.path.join(save_folder, "blur_" + filename), blurd)

    # Copy the label file and prepend the filename with "blur_"
    label_filename = os.path.splitext(filename)[0] + ".txt"
    with open(os.path.join(label_folder, label_filename), 'r') as f:
        label_content = f.read()
    with open(os.path.join(save_label_folder, "blur_" + label_filename), 'w') as f:
        f.write(label_content)
