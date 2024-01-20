"""Merge all downloaded images into a single PDF file"""
import os

from PIL import Image


def mergeImageToPDF(path: str, output_filename: str):
    """Merge all images in a directory into a single PDF file

    Args:
        - path (str): The path where the images are located
        - output_filename (str): The name of the output PDF file
    Returns:
        - None
    """
    image_files: list[str] = [
        f for f in os.listdir(path) if f.endswith('.jpg')]

    image_files.sort(key=lambda x: int(x.split('.')[0]))

    images = [Image.open(os.path.join(
        path, image_file)) for image_file in image_files]

    images = [image.convert('RGB') for image in images]

    images[0].save(output_filename, "PDF", resolution=100.0,
                   save_all=True, append_images=images[1:])
