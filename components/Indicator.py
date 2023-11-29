import customtkinter
from PIL import Image


class Indicator(customtkinter.CTkFrame):
    def __init__(self, master: any, text: str, img_path: str, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=0, pady=0)

        self.img = customtkinter.CTkImage(Image.open(img_path), size=(100, 100))
        self.label_img = customtkinter.CTkLabel(
            self, image=self.img, text="", width=50, height=50
        )
        self.label_img.grid(row=1, column=0, padx=10, pady=0)
