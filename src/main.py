import tkinter as tk
import requests
from mss import mss
import mss.tools
import pytesseract

def main():
    window.title("visual novel translation tool")
    window.configure(width=500, height=300)
    window.configure(bg='lightgray')
    window.attributes("-topmost", True)
    window.attributes("-alpha", 1)
    window.bind("<r>", change_transparency)
    window.bind("<s>", capture_screen) #TODO it is unclear why, but the position and size of the window changes (unintended) the first time only s is pressed.
    window.mainloop()

def change_transparency(event):
    if(window.attributes("-alpha") == 1):
        window.attributes("-alpha", 0)
    else:
        window.attributes("-alpha", 1)

def capture_screen(event):
    with mss.mss() as sct:
        window_size = {"top": window.winfo_y() + 43, "left": window.winfo_x() + 11,
         "width": window.winfo_width(), "height": window.winfo_height()} # The values don't seem to match up, so the adjustments were made manually
        output = "sct-{top}x{left}_{width}x{height}.png".format(**window_size)
        sct_img = sct.grab(window_size)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

if (__name__ == "__main__"):
    window = tk.Tk()
    main()
