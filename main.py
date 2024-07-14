from image_widgets import *
from PIL import Image
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('PhotoEdit')

        self.minsize(800, 500)
        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)

        # widgets
        # ImportButton
        ImageImport(self, self.import_image)
        # run
        self.mainloop()

    def import_image(self, path):
        try:
            # Use os.path.normpath to normalize the path
            normalized_path = os.path.normpath(path)
            # Open the image using a raw string
            self.image = Image.open(r"{}".format(normalized_path))
            self.image.show()
        except Exception as e:
            print(f"Error opening image: {e}")

if __name__ == "__main__":
    App()