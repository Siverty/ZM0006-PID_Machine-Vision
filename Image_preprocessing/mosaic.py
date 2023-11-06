import cv2
import os

def mosaic_images(train_folder, label_folder):
    # Loop through each image in the folder
    for filename in os.listdir(train_folder):
        # Check if the file name starts with "eroded_", "blur_", "mosaic_" or "noisy_"
        if filename.startswith("mosaic_"):
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

        elif filename.startswith("noisy_"):
            print(f"{filename} already mosaiced, skipping...")
            continue

        elif filename.startswith("negative_"):
            print(f"{filename} already negative, skipping...")
            continue

        # Load the image
        img = cv2.imread(os.path.join(train_folder, filename))

        # Define the size of the mosaic tiles
        tile_size = 3

        # Resize the image to a multiple of the tile size
        height, width, _ = img.shape
        new_height = height - (height % tile_size)
        new_width = width - (width % tile_size)
        img = cv2.resize(img, (new_width, new_height))

        # Create the mosaic image
        mosaic = cv2.resize(img, (int(new_width/tile_size), int(new_height/tile_size)), interpolation=cv2.INTER_AREA)
        mosaic = cv2.resize(mosaic, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

        # Save the mosaic image
        cv2.imwrite(os.path.join(train_folder, "mosaic_" + filename), mosaic)

        # Copy the label file and prepend the filename with "mosaic_"
        label_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(label_folder, label_filename), 'r') as f:
            label_content = f.read()
        with open(os.path.join(label_folder, "mosaic_" + label_filename), 'w') as f:
            f.write(label_content)

    print("process complete.")
    # The pipeline is finished, exit the program
    exit()
