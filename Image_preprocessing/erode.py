import cv2
import os

def erode_images(train_folder, label_folder):
    # Loop through each image in the folder
    for filename in os.listdir(train_folder):
        # Check if the file name starts with "eroded_", "blur_", "mosaic_" or "noisy_"
        if filename.startswith("eroded_"):
            os.remove(os.path.join(train_folder, filename))
            os.remove(os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt"))
            print(f"{filename} deleted...")
            continue

        elif filename.startswith("blur_"):
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

        # Define the kernel for erosion
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) # 5x5 kernel

        # Erode the image
        eroded = cv2.erode(img, kernel, iterations=1)

        # Save the eroded image
        cv2.imwrite(os.path.join(train_folder, "eroded_" + filename), eroded)

        # Copy the label file and prepend the filename with "eroded_"
        label_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(label_folder, label_filename), 'r') as f:
            label_content = f.read()
        with open(os.path.join(label_folder, "eroded_" + label_filename), 'w') as f:
            f.write(label_content)
