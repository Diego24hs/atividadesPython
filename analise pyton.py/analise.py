import pandas as pd
# passo 1 importar a base de dados
tabela= pd.read_csv("telecom_users.csv") 


# passo 2 visualizar a base de dados
      # -Entender as informaçoes excluir colunas e linhas desnecessarias 
      # axis 0= linhas    axis 1=coluna
    # - descobrir as cagadas da base de dados
tabela= tabela.drop("Unnamed: 0",axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"] , errors= "coerce")

tabela= tabela.dropna(how="all", axis=1)
tabela= tabela.dropna(how="any", axis=0)
print (tabela["Churn"].value_counts())
print (tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
import plotly.express as px

#criar o grafico
for coluna in tabela.columns:
  grafico= px.histogram(tabela, x= coluna, color="Churn", text_auto=True)
  #exibir o grafico
  grafico.show()
  
  


















# passo 3 tratamento de dados
# passo 5 analise detalhada