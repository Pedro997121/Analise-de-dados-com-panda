import pandas as pd
import re

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

#Descobrir quantidade de pessoas que cancelaram o plano, (Normalize=True recebe a informação em porcetagem, sem Normalize=True recebe a informação em quantidade)
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))