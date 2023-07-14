import cv2
import pytesseract
import numpy as np

def extract_text_from_image(image_binary):
    # Convert the binary data to a NumPy array
    nparr = np.frombuffer(image_binary, np.uint8)

    # Read the image using OpenCV
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Preprocess the image (grayscale, thresholding, etc.)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Perform text extraction using Tesseract OCR
    text = pytesseract.image_to_string(binary)

    return text
