import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):

        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('PhotoEdit')

        self.minsize(800,500)
        # run
        self.mainloop()


App()
