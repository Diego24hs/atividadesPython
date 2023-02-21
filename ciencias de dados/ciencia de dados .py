import pandas as pd
# importar a base de dados
tabela= pd.read_csv('advertising.csv')
print(tabela)
print(tabela.info)

# a correlação no exemplo vai de 0 a 1 mas o normal e de -1 a 1
#calcular a correlação da tabela
print(tabela.corr())
import matplotlib.pyplot as plt
import seaborn as sns
#criar grafico
sns.heatmap(tabela.corr(), cmap="Reds", annot=True)
plt.show()
# para selecionar uma coluna =[""]
# para selecionar uma lista de colunas [[ "","",]]
y=tabela["Vendas"] 
# é quem eu quero prever
x=tabela[["TV", "Radio", "Jornal"]]
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste= train_test_split(x, y, test_size=0.3)

# importar a inteligencia
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# criar inteligencia artificial
modelo_regressaolinear= LinearRegression()
modelo_arvoredecisao= RandomForestRegressor()

# treinar a inteligencia
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

previsao_regressaolinear= modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao= modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))

tabela_auxiliar= pd.DataFrame()
tabela_auxiliar["y_teste"]= y_teste
tabela_auxiliar["Previsao da Arvore de decisao"]= previsao_arvoredecisao
tabela_auxiliar["previsao RegressaoLinear"]= previsao_regressaolinear

sns.lineplot(data=tabela_auxiliar)
plt.show()


nova_tabela= pd.read_csv("novos.csv")
previsao= modelo_arvoredecisao.predict(nova_tabela)
print(previsao)