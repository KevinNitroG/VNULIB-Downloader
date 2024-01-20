"""Download all images of the book from a given URL of one page"""
import re
import os
import concurrent.futures

from requests import get

from requests import Response

folder_books_name: str = 'dowloaded_books'


def createNextBookFolderName(books_folder_path: str) -> str:
    """Create the next book folder name by finding the max book number in the path

    Args:
        - books_folder_path (str): The path where the book folders are located

    Returns:
        - next_book_folder (str): The name of the next book folder
    """
    folders: list[str] = os.listdir(books_folder_path)
    book_numbers: list[int] = [int(re.search(r'Book_(\d+)', folder).group(1))
                               for folder in folders if re.search(r'Bookz_(\d+)', folder)]
    max_book_number: int = max(book_numbers) if book_numbers else 0
    next_book_folder: str = f"Book_{max_book_number + 1}"
    return next_book_folder


def createJPGFileName(page_number: str) -> str:
    """Create JPG File Name By using the page number

    Args:
        - page_number (int):The number of p

    Returns:
        - jpg_file_name(str):the JPG file name
    """
    jpg_file_name = str(page_number)+'.jpg'
    return jpg_file_name


def dowloadImage(url: str) -> bytes:
    """Dowload Image from URL

    Args:
        - url (str):The URL of The Page

    Returns:
        - image_data(bytes):the data of the Image

    """
    response: Response = get(url, stream=True)
    response.raise_for_status()
    image_data: bytes = response.content
    return image_data


def saveImage(image_data: bytes, folder: str, file_name: str) -> None:
    """Save Image data to a file

    Args:
        - image_data (bytes): The data of the Image
        - folder (str): The path of the folder to save the image
        - file_name (str): The name of the file to save the image

    Returns:
        - None
    """
    # Write the image data to a file in the specified folder
    with open(os.path.join(folder, file_name), 'wb') as file:
        file.write(image_data)


def downloadAllImages(url: str, path: str):
    """Download all images from a URL and save them in a book folder

    Args:
        - url (str): The URL to download images from
        - path (str): The path to create the book folder in

    """
    book_folder: str = createNextBookFolderName(path)
    book_path: str = os.path.join(path, book_folder)
    os.makedirs(book_path, exist_ok=True)
    futures: list = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for page_number in range(1, 10000):
            try:
                current_url: str = re.sub(
                    r'page=\d+', f'page={page_number}', url)
                futures.append(executor.submit(dowloadImage, current_url))
            except Exception as e:
                if 'Error:Error converting document' in str(e):
                    break
                else:
                    print(f"An error occurred: {e}")
                    continue
        for i, future in enumerate(futures, start=1):
            try:
                image_data: bytes = future.result()
                image_file_name: str = createJPGFileName(i)
                saveImage(image_data, book_path, image_file_name)
            except Exception as e:
                print(f"An error occurred while saving image: {e}")


def dowloadAllImagesFromAllLinks(LINKS: list[str], path: str) -> None:
    """Dowload All Images From All Links Input

        Args:
            -LINKS (list[str]):list of links input
            -path (str):The path provide to put the folder

        Returns:
            -None
    """
    for link in LINKS:
        downloadAllImages(link, path)
