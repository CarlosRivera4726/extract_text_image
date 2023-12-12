from PIL import Image
import pytesseract

# path to tesseract orc
pytesseract.pytesseract.tesseract_cmd = r'E:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class TextExtract(object):
    def __init__(self, image_path):
        self.image_path = image_path
    
    def load_image(self):
        img = Image.open(self.image_path)
        return self.extract_text(img)
    def extract_text(self, img):
        return pytesseract.image_to_string(img)
