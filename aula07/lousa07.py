import pandas as pd

dados = {
    "nome": ["joão", "marta" , "ary" , "matheus" , "michelle"],
    "idade": [51,37,23,24,33]
}

df = pd.DataFrame(data = dados)

print(df)
