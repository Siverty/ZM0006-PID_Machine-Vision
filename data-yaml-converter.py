import yaml
import os

# Load the original data.yaml file
with open('data-old.yaml', 'r') as file:
    original_data = yaml.safe_load(file)

# Load the updated data.yaml file
with open('data.yaml', 'r') as file:
    updated_data = yaml.safe_load(file)

# Create a mapping from class names to their corresponding indices in the original data.yaml
original_class_mapping = {class_name: idx for idx, class_name in enumerate(original_data['names'])}

# Create a mapping from class indices in the updated data.yaml to their corresponding names
updated_class_mapping = {idx: class_name for idx, class_name in enumerate(updated_data['names'])}

# Directory containing the .txt files
txt_folder = 'datasets/dataset3/train/labels'

# Process each .txt file in the folder
for txt_file_name in os.listdir(txt_folder):
    if txt_file_name.endswith('.txt'):
        txt_file_path = os.path.join(txt_folder, txt_file_name)

        with open(txt_file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split(' ')
            if len(parts) >= 1:
                original_class_idx = int(parts[0])
                if original_class_idx in original_class_mapping:
                    updated_class_name = updated_class_mapping[original_class_mapping[original_class_idx]]
                    parts[0] = str(updated_data['names'].index(updated_class_name))
                    new_lines.append(' '.join(parts))

        # Write the updated lines back to the .txt file
        with open(txt_file_path, 'w') as file:
            file.write('\n'.join(new_lines))