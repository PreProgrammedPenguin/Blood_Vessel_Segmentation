from PIL import Image
import os

def convert_images_to_jpg(input_folder):
    # Traverse the folder structure
    for root, _, files in os.walk(input_folder):
        for file in files:
            input_path = os.path.join(root, file)
            # Check the file extension to process only image files
            if True:
                output_path = os.path.splitext(input_path)[0] + ".jpg"
                try:
                    with Image.open(input_path) as img:
                        img = img.convert("RGB")  # Ensure compatibility with JPEG
                        img.save(output_path, "JPEG")
                        print(f"Converted: {input_path} -> {output_path}")
                    os.remove(input_path)  # Remove the original file after conversion
                except Exception as e:
                    print(f"Failed to convert {input_path}: {e}")

# Folder structure
base_folder = r'D:\User Data\Downloads\my_dataset'
subfolders = ["training/images", "training/masks", "test/images", "test/masks"]

# Convert images in each subfolder
for subfolder in subfolders:
    convert_images_to_jpg(os.path.join(base_folder, subfolder))
