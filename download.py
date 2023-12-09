import tarfile
import os
from urllib.request import urlretrieve

os.chdir("C:\\Program Files\\textractor\\tesseract")

# get tesseract tar.gz in C:\Program Files\Tesseract-OCR, extract to C:\Program Files\Tesseract-OCR\tesseract.exe
URL = "https://download.sourceforge.net/tesseract-ocr-alt/tesseract-ocr-3.02.grc.tar.gz"
urlretrieve(URL, "tesseract-ocr-3.02.grc.tar.gz")
tar = tarfile.open("tesseract-ocr-3.02.grc.tar.gz", "r:gz")
tar.extractall()
tar.close()

# download 
os.chdir("C:\\Program Files\\textractor\\bin")
