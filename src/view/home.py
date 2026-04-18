import customtkinter

class Home(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.entry()

    def entry(self):
        inputson = customtkinter.CTkEntry(self, placeholder_text='CTkEntry', width=140, height=28)
        inputson.place(x=10, y=10)