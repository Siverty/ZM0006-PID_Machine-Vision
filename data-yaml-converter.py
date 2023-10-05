import yaml

# Load the original data.yaml file
with open('original_data.yaml', 'r') as file:
    original_data = yaml.safe_load(file)

# Load the updated data.yaml file
with open('updated_data.yaml', 'r') as file:
    updated_data = yaml.safe_load(file)

# Create a mapping from class names to their corresponding indices in the original data.yaml
original_class_mapping = {class_name: idx for idx, class_name in enumerate(original_data['names'])}

# Create a mapping from class indices in the updated data.yaml to their corresponding names
updated_class_mapping = {idx: class_name for idx, class_name in enumerate(updated_data['names'])}

# Process each .txt file
for txt_file_name in ['file1.txt', 'file2.txt', 'file3.txt']:  # Replace with your file names
    with open(txt_file_name, 'r') as file:
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
    with open(txt_file_name, 'w') as file:
        file.write('\n'.join(new_lines))