import cv2
import os
import numpy as np

def add_noise(train_folder, label_folder):
    # Loop through each image in the folder
    for filename in os.listdir(train_folder):
        # Check if the file name starts with "eroded_", "blur_", "mosaic_" or "noisy_"
        if filename.startswith("noisy_"):
            os.remove(os.path.join(train_folder, filename))
            os.remove(os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt"))
            print(f"{filename} deleted...")
            continue

        elif filename.startswith("eroded_"):
            print(f"{filename} already eroded, skipping...")
            continue

        elif filename.startswith("blur_"):
            print(f"{filename} already blurred, skipping...")
            continue

        elif filename.startswith("mosaic_"):
            print(f"{filename} already mosaiced, skipping...")
            continue

        # Load the image
        img = cv2.imread(os.path.join(train_folder, filename))

        # Define the kernel for erosion
        kernel = (9, 9) # 9x9 kernel for blurring

        # Add Gaussian noise to the image
        mean = 0
        var = 2000
        sigma = var ** 0.5
        gaussian = np.random.normal(mean, sigma, img.shape)
        noisy_image = np.clip((img + gaussian), 0, 255).astype(np.uint8)

        # Save the noisy image
        cv2.imwrite(os.path.join(train_folder, "noisy_" + filename), noisy_image)

        # Copy the label file and prepend the filename with "noisy_"
        label_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(label_folder, label_filename), 'r') as f:
            label_content = f.read()
        with open(os.path.join(label_folder, "noisy_" + label_filename), 'w') as f:
            f.write(label_content)
