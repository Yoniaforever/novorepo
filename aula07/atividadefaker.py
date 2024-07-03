"""
Uma função para criar personas, contendo nome, cidade, idade. 
Salve os dados dessas personas em um arquivo CSV.
Suba todos os arquivos para seu repositório.

"""


from faker import Faker
import pandas as pd


fake = Faker('pt_BR')



 

def create_persona() -> dict:
    data = {
    "nome": fake.name(),
    "cidade": fake.city(),
    "idade": fake.random_int(18, 100)
    }
    return data


def generate_personas_qtd(number_of_personas: int) -> list:
    # personas_list = []
    # for _ in range(number_of_personas):
    #     personas_list.append(create_persona())
# LIST COMPREHENSION 
#operadores ternários
    return [create_persona() for _ in range(number_of_personas)]





lista_de_personas = generate_personas_qtd(3)    


def create_df(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    return df

df_lista_de_personas = create_df(lista_de_personas)

print(df_lista_de_personas)

def save_to_csv(filename: str, dataframe: pd.DataFrame) -> None:
    dataframe.to_csv(filename, index=False)

df_lista_de_personas.to_csv('lista_de_personas.csv', index=False)

save_to_csv(filename='lista_de_personas.csv', dataframe=df_lista_de_personas)