import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
from PIL import Image

# PNG görüntüsünü yükleyin
image_path = "D:/Users/SEMAH/Desktop/imageToText/testocr.png"
image = Image.open(image_path)

# Görüntüdeki metni okuyun
text = pytesseract.image_to_string(image, lang='eng')

# Metni bir metin dosyasına yazın
output_file = "metin_dosyasi.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)

print("Metin dosyası oluşturuldu:")
