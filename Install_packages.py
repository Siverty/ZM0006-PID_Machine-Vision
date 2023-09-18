import subprocess

# List of packages to check and install
packages = [
    "tabulate",
    "ultralytics",
    "roboflow",
    "numpy",
    "torch",
    "torchvision",
    "matplotlib",
    "scikit-image",
    "torch",
    "sklearn",
    "scipy",
    "opencv-python",
    "pillow",
    "pyyaml",
    "tqdm",
    "requests",
    "opencv-python-headless",
    "gitpython",
    "setuptools",
    "IPython",
]


# Function to check if a package is installed
def check_package_installed(package):
    try:
        # Use subprocess to run the command and capture the output
        result = subprocess.run(
            ["pip", "show", package], capture_output=True, text=True
        )

        # Check the return code of the subprocess command
        if result.returncode == 0:
            # Package is installed
            return True
        else:
            # Package is not installed
            return False
    except Exception as e:
        print(f"An error occurred while checking package '{package}': {str(e)}")
        return False


# Function to install a package
def install_package(package):
    try:
        # Use subprocess to run the command and capture the output
        subprocess.run(["pip", "install", package])
        return "Newly Installed"
    except Exception as e:
        return f"Error: {str(e)}"

# Check package status
package_status = []
for package in packages:
    if check_package_installed(package):
        package_status.append([package, "✓", ""])
    else:
        package_status.append([package, "", "✓"])
        install_package(package)

from tabulate import tabulate

# Generate output table
table_headers = ["Package", "Already Installed", "Newly Installed"]
output_table = tabulate(package_status, headers=table_headers, tablefmt="grid")

# Print the output table
print(output_table)
