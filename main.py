# from .src.controller.busca import busca_cnpj
from src.view.home import Home

if __name__ == '__main__':

    app = Home()
    app.mainloop()
    # busca = busca_cnpj()
    # busca.iniciar()
    # busca.busca()
    
