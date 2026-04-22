

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import json


if __name__ == "__main__":
    cnpj = sys.argv[1]  # Recebe do Tauri
    
    try:
        driver = webdriver.Edge()
        driver.get('https://google.com')
        # ... faça sua busca com Selenium ...
        driver.quit()
        
        # IMPORTANTE: Retornar em JSON
        resultado = {
            "cnpj": cnpj,
            "status": "sucesso",
            "dados": ["Busca realizada com sucesso"]
        }
        print(json.dumps(resultado, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"erro": str(e)}))
        sys.exit(1)
