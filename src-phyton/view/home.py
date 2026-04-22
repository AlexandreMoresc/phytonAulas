import customtkinter

class Home(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.entry()

    def acoes(self, event=None):
        valor = self.inputson
        
        if not valor:
            print("campo vazio")
            return
        
           

    def entry(self):
        self.inputson = customtkinter.CTkEntry(self, placeholder_text='CNPJ', width=200, height=32)
        self.inputson.place(x=20, y=10)
        self.inputson.get()
        self.inputson.bind("<Enter>", self.acoes)