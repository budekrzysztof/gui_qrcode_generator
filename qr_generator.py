# 2021 Krzysztof Budek

import tkinter as tk
import qrcode
import os

from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter.font import Font

class qr_generator:
    def retrieve_input(self):
        input_value = self.text_box.get("1.0", "end-1c")

        self.img = qrcode.make(input_value).resize((240, 240), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(self.img)

        self.panel.configure(image=new_image)
        self.panel.image = new_image

    def download_image(self):
        path = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")

        if not path:
            return

        self.img.convert('RGB').save(path)

    def __init__(self):
        # create window
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        self.root.resizable(0,0)

        self.canvas = tk.Canvas(self.root, height=600, width=800, bg="#ECE4DB")
        self.canvas.pack()

        # div for whole content that will be split in two halves
        self.workspace = tk.Frame(self.root, bg="#ECE4DB")
        self.workspace.place(relwidth=0.7, relheight=0.65, rely=0.15, relx=0.15)

        # left side of content div
        self.left_workspace = tk.Frame(self.workspace, bg="#ECE4DB")
        self.left_workspace.place(relwidth=0.5, relheight=1)

        # text input
        self.text_box = tk.Text(self.left_workspace, height=15, width=30)
        self.text_box.pack(pady=29)

        # right side of content div
        self.right_workspace = tk.Frame(self.workspace, bg="#ECE4DB")
        self.right_workspace.place(relwidth=0.5, relheight=1, relx=0.5)

        self.img = (Image.open("image/frame.png")).resize((240, 240), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(self.img)

        self.panel = tk.Label(self.right_workspace, image=new_image)
        self.panel.pack(side = "top", fill = "none", expand = "no", pady=29)

        # create download button
        self.download_button = tk.Button(self.right_workspace, height=3, width=30, text='Download',
                                        command=self.download_image)
        self.download_button.pack(side='left', padx=45)

        # create QR button
        self.button_commit = tk.Button(self.left_workspace, height=3, width=30, text='Generate',
                                    command=self.retrieve_input)
        self.button_commit.pack(side='left', padx=45)

        # run root mainloop
        self.root.mainloop()

george = qr_generator()

