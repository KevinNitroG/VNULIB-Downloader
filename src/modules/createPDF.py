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
    image_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    images = [Image.open(os.path.join(
        path, image_file)) for image_file in image_files]
    images = [image.convert('RGB') for image in images]
    images[0].save(output_filename, 'PDF', resolution=100.0,
                   save_all=True, append_images=images[1:])


def createPDFInSubdirectories(path):
    """Merge all The Images To PDF

        Args:
            - path (str): The path where the images are located

        Return:

            - None 
    """
    subdirectories: list = [os.path.join(path, d) for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]
    for subdirectory in subdirectories:
        if any(file.endswith('.pdf') for file in os.listdir(subdirectory)):
            continue
        output_filename = os.path.join(
            subdirectory, os.path.basename(subdirectory) + '.pdf')
        mergeImageToPDF(subdirectory, output_filename)
