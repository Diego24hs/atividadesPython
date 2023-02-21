from selenium import webdriver
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Edge()
# para escolher o elemento no navegador= navegador.find_element("xpath", 
# .click=clicar
# .send_keys= escrever dentro                                   
# . get= pegar uma informação dentro 
# passo 1 pegar a cotacao do dolar
navegador.get("https://www.google.com.br/")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação do dolar")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# passo 2 pegar a cotacao do euro
navegador.get("https://www.google.com.br/")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("cotação do euro")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# passo 3 pegar a cotacao do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro= navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro= cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

# importar a base de dados e atualizar a base
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
# recalcular os preços
tabela.loc[tabela["Moeda"]== "Dólar", "Cotação"]= float(cotacao_dolar)
tabela.loc[tabela["Moeda"]== "Euro", "Cotação"]= float(cotacao_euro)
tabela.loc[tabela["Moeda"]== "Ouro", "Cotação"]= float(cotacao_ouro)
tabela["Preço de Compra"]= tabela["Cotação"]* tabela["Preço Original"]
tabela["Preço de Venda"]= tabela["Preço de Compra"]* tabela["Margem"]


print(tabela)
# exportar a base atualizad
tabela.to_excel("Produtos editados.xlsx", index= False)
