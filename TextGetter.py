from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Users\marvi\Downloads\Document 7.docx"
image_path = r"C:\Users\marvi\Downloads\Document 7.docx"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)

print(text[:-1])