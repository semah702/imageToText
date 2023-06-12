# imageToText

imageToText is a python script that uses pytesseract to convert images to text with OCR.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pytesseract
```

And install [Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html) for your OS.
[(Tesseract OCR Main Repository)](https://github.com/tesseract-ocr/tesseract)

## Usage

`run.py` is the main script. It takes in a path to an image and outputs the text in the image.

Define the path to the image in `run.py`:
```python
# Add image path from your local computer
image_path = "testocr.png"
```

And run the script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)