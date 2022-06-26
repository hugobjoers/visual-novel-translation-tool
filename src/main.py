import tkinter as tk
import requests
from mss import mss
import mss.tools
import time
from PIL import Image
import pytesseract


def main():
    window.title("visual novel translation tool")
    #window.configure(width=500, height=300)
    window.configure(bg='lightgray')
    window.attributes("-topmost", True)
    window.attributes("-alpha", 1)
    window.bind("<r>", change_transparency)
    # TODO it is unclear why, but the position and size of the window changes (unintended) the first time only s is pressed.
    window.bind("<s>", capture_screen)
    window.bind("<c>", convert_image_to_text)
    window.mainloop()


def change_transparency(event):
    if(window.attributes("-alpha") == 1):
        window.attributes("-alpha", 0)
    else:
        window.attributes("-alpha", 1)


def capture_screen(event):
    with mss.mss() as sct:
        window_size = {"top": window.winfo_y() + 43, "left": window.winfo_x() + 11,
                       "width": window.winfo_width(), "height": window.winfo_height()}  # The values don't seem to match up, so the adjustments were made manually
        output = "screen_capture.png"
        sct_img = sct.grab(window_size)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def convert_image_to_text(event):
    pass
    text_file = open("text.txt", "w")
    text = pytesseract.image_to_string(Image.open("screen_capture.png"))
    text_file.write(text)
    text_file.close()


if (__name__ == "__main__"):
    window = tk.Tk()
    # your path may be different
    pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
    main()
