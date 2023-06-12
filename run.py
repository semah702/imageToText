from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# Manually dd tesseract path manual to your system environment variables
# pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Add image path from your local computer
image_path = "testocr.png"
image = Image.open(image_path)

# Read text from image
text = pytesseract.image_to_string(image, lang='eng')

# Save text to file
output_file = "output.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)

print("Generated text file: ", output_file)
