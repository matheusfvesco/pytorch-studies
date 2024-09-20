import cv2
import numpy as np
import argparse

def set_alpha_to_zero_on_white(image_path: str, suffix: str):
    # Read the image in BGR color space
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Ensure we load with alpha if present
    
    # Check if image has an alpha channel, if not, add one
    if image.shape[2] == 3:
        # Add alpha channel (fully opaque)
        image_bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    else:
        image_bgra = image
    
    # Get all white pixels (BGR value of [255, 255, 255])
    white_pixels = np.all(image_bgra[:, :, :3] == [255, 255, 255], axis=-1)
    
    # Set the alpha channel of white pixels to 0
    image_bgra[white_pixels, 3] = 0
    
    # Save the modified image with a specified suffix
    output_path = image_path.replace('.png', f'{suffix}.png')
    cv2.imwrite(output_path, image_bgra)

def main():
    parser = argparse.ArgumentParser(description='Set Alpha Channel of White Pixels to Zero in Images and Add a Suffix to Output Files')
    
    # Add an optional argument for the suffix
    parser.add_argument(
        '--suffix',
        type=str,
        help='Suffix to be added to the output files',
        default="_nobkg"
    )
    
    # Add an optional argument for multiple images paths
    parser.add_argument('image_paths', type=str, nargs='+', help='Path to the image files')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Process each provided image path
    for image_path in args.image_paths:
        set_alpha_to_zero_on_white(image_path, args.suffix)

if __name__ == "__main__":
    main()