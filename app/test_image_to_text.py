from image_to_text import extract_text_from_image
import pytest
from unittest.mock import MagicMock
import os
import cv2
import numpy as np


def test_extract_text_from_image():
    # Create a sample image for testing
    image_path = 'test_image.png'
    image = np.ones((100, 100, 3), dtype=np.uint8)
    text = 'Test'
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (10, 50), font, 1, (0, 0, 0), 2)

    cv2.imwrite(image_path, image)

    # Read the image file as binary data
    with open(image_path, 'rb') as f:
        image_binary = f.read()

    # Call the function
    result = extract_text_from_image(image_binary)

    # Assertions
    assert result == 'Test\n'

    # Clean up the test image file
    os.remove(image_path)

def test_extract_text_from_image_from_file():
    # Specify the path to the test image file
    image_path = './data/test.png'

    # Read the image file as binary data
    with open(image_path, 'rb') as f:
        image_binary = f.read()

    # Call the function
    result = extract_text_from_image(image_binary)

    # Assertions
    assert 'SAMPLE PNG' in result
    assert 'FILE' in result

