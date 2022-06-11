import tkinter as tk
import requests
from mss import mss
import pytesseract

# with mss() as sct:
#     sct.shot()


def main():
    window.title("visual novel translation tool")
    window.configure(width=500, height=300)
    window.configure(bg='lightgray')
    window.attributes("-topmost", True)
    window.attributes("-alpha", 1)
    window.bind("<r>", change_transparency) 
    
    window.mainloop()

def change_transparency(event):
    if(window.attributes("-alpha") == 1):
        window.attributes("-alpha", 0)
    else:
        window.attributes("-alpha", 1)



if (__name__ == "__main__"):
    window = tk.Tk()
    main()
