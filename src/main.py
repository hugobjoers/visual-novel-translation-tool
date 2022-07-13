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
    window.bind("<c>", translate_screen_capture)
    stay_in_focus()
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


def translate_screen_capture(event):
    text = convert_image_to_text()
    translate_text(text)


def convert_image_to_text():
    text = pytesseract.image_to_string(
        Image.open("screen_capture.png"), lang="jpn")
    return text


def translate_text(text):
    print(text)
    data = {
        "source_lang": "JA",
        "target_lang": "EN-US",
        "auth_key": auth_key,
        "text": text,
    }
    result = requests.post("https://api-free.deepl.com/v2/translate", data=data)
    print(result.status_code)
    translation = result.json()["translations"][0]["text"]
    print(translation)
    return translation


def stay_in_focus():
    window.focus_force()
    window.after(200, stay_in_focus)


def read_api_key():
    with open("src/apikey.txt") as f:
        auth_key = f.readline()
        return auth_key


if (__name__ == "__main__"):
    window = tk.Tk()
    # your path may be different
    pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
    auth_key = read_api_key()
    main()
