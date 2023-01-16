# importing tkinter for gui
import tkinter as tk

from PIL import ImageTk, Image
import assistant as sp

def app():
    # creating window
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # setting attribute
    window.attributes('-fullscreen', True)
    # window.title("Geeks For Geeks")

    imgTemp = Image.open("res/images/asst-bg.jpg")
    img2 = imgTemp.resize((width,height))
    img = ImageTk.PhotoImage(img2)

    label1 = tk.Label(window,image=img)
    label1.pack(side='top',expand=True)

    window.after(1000, sp.welcomeSpeak())
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app()
