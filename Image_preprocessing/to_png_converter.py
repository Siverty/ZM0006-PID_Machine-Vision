import os
from PIL import Image

def any_to_png_converter(train_folder):
    for filename in os.listdir(train_folder):
        if not filename.endswith(".png"):
            print("converting " + filename + " to png")
            img = Image.open(os.path.join(train_folder, filename))
            new_filename = os.path.splitext(filename)[0] + ".png"
            img.save(os.path.join(train_folder, new_filename))
            os.remove(os.path.join(train_folder, filename))

    print("Conversion and deletion complete.")
