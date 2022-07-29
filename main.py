
import plotly.express as px
import pandas as pd

numero = []

#ler a tabela
tabela = pd.read_csv("telecom_users.csv")

#remover informações inuteis
tabela = tabela.drop("Unnamed: 0", axis=1,)

#Trocar coluna de string pra int/float
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors='coerce')

#remover clientes com informações faltando
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

#informação sobre a tabela
print(tabela.info())

#resultado em forma de grafico
grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn", text_auto=True)
grafico.show()