import argparse
from PIL import Image

def crop_and_resize(image_path: str, suffix: str, new_width: int):
    # Load the image
    img = Image.open(image_path)
    
    # Ensure image has an alpha channel
    if img.mode != 'RGBA':
        raise ValueError("Image does not have an alpha channel")

    # Extract the alpha channel
    alpha = img.split()[-1]

    # Get the bounding box of non-zero alpha regions
    bbox = alpha.getbbox()

    # If there's no non-zero alpha region, return None
    if bbox:
        # Crop the image to this bounding box
        cropped_img = img.crop(bbox)
        
        # Resize the image while maintaining aspect ratio
        width_percent = new_width / float(cropped_img.size[0])
        new_height = int((float(cropped_img.size[1]) * width_percent))
        
        resized_img = cropped_img.resize((new_width, new_height), Image.BICUBIC)
        output_path = image_path.replace(".png", f"{suffix}.png")
        resized_img.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crop and resize images.")
    
    parser.add_argument(
        'images', 
        nargs='+',
        type=str, 
        help='Paths to the input images'
    )
    parser.add_argument(
        '--suffix', 
        default='_crop',
        help='Suffix to add to the output files'
    )
    parser.add_argument(
        '--new_width', 
        type=int, 
        default=700,
        help='New width for the resized image'
    )

    args = parser.parse_args()

    for image_path in args.images:
        crop_and_resize(image_path, args.suffix, args.new_width)