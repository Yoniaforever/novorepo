import pandas as pd

dados = pd.read_csv("./dados_ficticios.csv")

df = pd.DataFrame(dados)

maiores_de_40 = df[df["idade"] >= 40]

renda_5mil = df[df["renda"] >= 5000]

renda_15mil = df[df["renda"] >= 15000]

print(maiores_de_40)
print(renda_15mil)
print(renda_5mil)

