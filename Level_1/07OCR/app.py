from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def ocr_image(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = 'example.jpg'
    extracted_text = ocr_image(image_path)
    print("Extracted Text:")
    print(extracted_text)
