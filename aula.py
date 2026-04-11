from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class busca_cnpj():    

    def iniciar(self):
        self.driver = webdriver.Chrome()

    def busca(self):
        driver = self.driver
        self.driver.get('https://google.com')
        cnpj = driver.find_element(By.CLASS_NAME, 'gLFyf')
        cnpj.send_keys('04.266.331/0019-58' + Keys.ENTER)

if __name__ == '__main__':
    busca = busca_cnpj()
    busca.iniciar()
    busca.busca()
