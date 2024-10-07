from PIL import Image
import os

def read_jpeg_file():
    while True:
        file_path = input("Enter the path to your JPEG file: ")
        if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg')):
            return file_path
        else:
            print("Invalid file path or not a JPEG file. Please try again.")

def convert_jpeg_to_png(jpeg_path):
    try:
        with Image.open(jpeg_path) as img:
            return img.convert('RGB')
    except Exception as e:
        print(f"Error converting image: {str(e)}")
        return None

def save_png_file(img, original_path):
    try:
        # Create the output filename by changing the extension to .png
        output_path = os.path.splitext(original_path)[0] + ".png"
        img.save(output_path, 'PNG')
        print(f"PNG file saved successfully as: {output_path}")
        return True
    except Exception as e:
        print(f"Error saving PNG file: {str(e)}")
        return False

def main():
    # Start
    print("JPEG to PNG Converter")

    # Read JPEG file
    jpeg_path = read_jpeg_file()

    # Convert JPEG to PNG
    png_image = convert_jpeg_to_png(jpeg_path)
    if png_image is None:
        print("Conversion failed. Exiting.")
        return

    # Save PNG file
    if save_png_file(png_image, jpeg_path):
        print("Conversion completed successfully.")
    else:
        print("Failed to save PNG file.")

    # End
    print("Process completed.")

if __name__ == "__main__":
    main()
