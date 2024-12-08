import os
from PIL import Image, ImageEnhance

def resize_and_enhance_images(input_folder, output_folder, target_size=(512, 512)):
    """
    Resizes and enhances the quality of images in the specified folder.
    
    :param input_folder: Path to the folder containing input images.
    :param output_folder: Path to the folder where processed images will be saved.
    :param target_size: Tuple specifying the target size (width, height).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')):
            try:
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                
                # Open the image
                with Image.open(input_path) as img:
                    # Resize the image
                    img_resized = img.resize(target_size, Image.ANTIALIAS)
                    
                    # Enhance the image quality
                    enhancer = ImageEnhance.Sharpness(img_resized)
                    img_enhanced = enhancer.enhance(1.5)  # Adjust sharpness factor as needed
                    
                    # Save the processed image
                    img_enhanced.save(output_path, quality=95)  # Save with high quality
                    print(f"Processed and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_folder = "img/img2"
output_folder = "img"
resize_and_enhance_images(input_folder, output_folder, target_size=(512, 512))
