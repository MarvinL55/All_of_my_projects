from PIL import Image
from pytesseract import pytesseract


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\\Users\\marvi\\OneDrive\\Pictures\\second.png"
image_path2 = r"C:\\Users\\marvi\\OneDrive\\Pictures\\textpicture.png"

img = Image.open(image_path)
img2 = Image.open(image_path2)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)
text2 = pytesseract.image_to_string(img2)

print(text[:-1])
print(text2[:-1])