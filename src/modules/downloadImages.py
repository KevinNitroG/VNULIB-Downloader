import os
import re
import concurrent.futures
import requests


from alive_progress import alive_bar

from requests import get

from requests import Response

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def createNextBookFolderName(books_folder_path: str) -> str:
    """Create the next book folder name by finding the max book number in the path

    Args:
        - books_folder_path (str): The path where the book folders are located

    Returns:
        - next_book_folder (str): The name of the next book folder
    """
    folders: list[str] = os.listdir(books_folder_path)
    book_numbers: list[int] = []
    for folder in folders:
        match = re.search(r'Book_(\d+)', folder)
        if match is not None:
            book_numbers.append(int(match.group(1)))
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


def dowloadImage(url: str, file_path: str) -> None:
    """Download an image and save it to a file

    Args:
        - url (str): The URL to download the image from
        - file_path (str): The path to save the image to
    """
    try:
        # Add timeout argument
        response: Response = get(url, stream=True, verify=False, timeout=10)
        response.raise_for_status()

        with open(file_path, 'wb') as f:
            f.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def getTextFromURL(url: str) -> str:
    """Get text content from a URL

    Args:
        - url (str): The URL to get text from

    Returns:
        - text (str): The text content of the URL
    """
    try:
        response: Response = get(url, verify=False, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return ""


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

    Params:
        - url (str): The URL to download images from
        - path (str): The path to create the book folder in

    """
    book_folder: str = createNextBookFolderName(path)
    book_path: str = os.path.join(path, book_folder)
    os.makedirs(book_path, exist_ok=True)
    futures: list = []
    page_number = 1
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        while True:
            try:
                current_url: str = re.sub(
                    r'page=\d+', f'page={page_number}', url)
                text: str = getTextFromURL(current_url)
                if "Error:Error converting document" in text:
                    break
                file_name = f"image_{page_number}.jpg"
                file_path = os.path.join(book_path, file_name)
                futures.append(executor.submit(
                    dowloadImage, current_url, file_path))
            except requests.exceptions.RequestException as e:
                if 'Error:Error converting document' in str(e):
                    break
                else:
                    print(f"An error occurred: {e}")
                    continue
            page_number += 1


def dowloadAllImagesFromAllLinks(LINKS: list[str] | None) -> None:
    """Dowload All Images From All Links Input

        Args:
            -LINKS (list[str]):list of links input
            -path (str):The path provide to put the folder

        Returns:
            -None
    """
    if LINKS is None:
        return
    for link in LINKS:
        downloadAllImages(link, os.path.join(os.getcwd(), 'dowloaded_books'))
