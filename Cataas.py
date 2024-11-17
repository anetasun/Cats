from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
Label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    # Устанавливаем изображение в метку
    label.config(image=img)
    # Необходимо сохранить ссылку на изображение, чтобы избежать сборки мусора
    label.image = img

window.mainloop()

