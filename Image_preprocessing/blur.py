import cv2
import os

def blur_images(train_folder, label_folder):
    # Loop through each image in the folder
    for filename in os.listdir(train_folder):
        # Check if the file name starts with "eroded_", "blur_", "mosaic_" or "noisy_"
        if filename.startswith("blur_"):
            os.remove(os.path.join(train_folder, filename))
            os.remove(os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt"))
            print(f"{filename} deleted...")
            continue

        elif filename.startswith("eroded_"):
            print(f"{filename} already blurred, skipping...")
            continue

        elif filename.startswith("noisy_"):
            print(f"{filename} already noisy, skipping...")
            continue

        elif filename.startswith("mosaic_"):
            print(f"{filename} already mosaiced, skipping...")
            continue

        # Load the image
        img = cv2.imread(os.path.join(train_folder, filename))

        # Define the kernel for blurring
        kernel = (9, 9)  # 9x9 kernel for blurring

        # Blur the image
        blurred = cv2.GaussianBlur(img, kernel, 0)

        # Save the blured image
        cv2.imwrite(os.path.join(train_folder, "blur_" + filename), blurred)

        # Copy the label file and prepend the filename with "blur_"
        label_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(label_folder, label_filename), 'r') as f:
            label_content = f.read()
        with open(os.path.join(label_folder, "blur_" + label_filename), 'w') as f:
            f.write(label_content)
