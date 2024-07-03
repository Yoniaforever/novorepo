import pandas as pd

dados = {
    "nome": ["matheus" , "carlinhos" , "rico" , "el primo" , "giorno" , "Luiza" , "jane"],
    "idade": [33,25,28,34,45,16,1908],
    "cidade": ["Recife" , "Recife" ,"Recife" , "salvador" , "salvador" , "manaus" , "são paulo"]
}

df = pd.DataFrame(dados)
moradores_recife = df[df["cidade"] == "Recife"]

print("Moradores do Recife:")
print(moradores_recife)