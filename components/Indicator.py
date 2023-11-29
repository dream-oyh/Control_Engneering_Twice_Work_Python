import customtkinter
from PIL import Image


class Indicator(customtkinter.CTkFrame):
    """
    指示当前处于哪一个 tab
    """

    def __init__(self, master: any, text: str, img_path: str, **kwargs):
        super().__init__(master, **kwargs)
        self.img = customtkinter.CTkImage(Image.open(img_path), size=(100, 100))
        self.label_img = customtkinter.CTkLabel(
            self,
            image=self.img,
            text=text.split(maxsplit=1)[0],
            width=50,
            height=50,
            text_color="#000000",
        )
        self.label_img.grid(row=0, column=0, padx=0, pady=0)
