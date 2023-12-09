import os
from pathlib import Path

import typer
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app = typer.Typer()


@app.command()
def extract(filepath: str, outfile: str = "", autoFile: bool = False):
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist")
        return

    if os.path.isdir(filepath):
        print(f"File {filepath} is a directory")
        return

    text = pytesseract.image_to_string(Image.open(filepath))

    if autoFile:
        outfile = (
            "./" + Path(filepath).stem + ".txt".replace(" ", "_").replace("_data", "")
        )

    if outfile:
        if not os.path.exists(outfile):
            open(outfile, "w").close()

        if not os.path.exists(outfile):
            print(f"File {outfile} could not be created")
            return

        if os.path.isdir(outfile):
            print(f"File {outfile} is a directory")
            return
        with open(filepath, "w") as f:
            f.write(text)
        print(f"Saved to {outfile}")
    else:
        print(text)


if __name__ == "__main__":
    app()
