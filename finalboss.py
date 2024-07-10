import requests
import json
from faker import Faker

fake = Faker('pt_BR')

username = fake.user_name()
email = fake.email()
password = fake.password()
telefone = fake.phone_number()
endereco = fake.address()
cpf = fake.cpf()

user_data = {
    "username": username,
    "email": email,
    "password": password,
    "phone": telefone,
    "address": endereco,
    "cpf": cpf
}

print (user_data)

create_user_url = 'https://desafiopython.jogajuntoinstituto.org/api/users/'
login_url = 'http://desafiopython.jogajuntoinstituto.org/api/users/login/'

ordered_user_data = sorted(user_data.items(), key=lambda x: ["username", "email", "password", "phone", "address", "cpf"].index(x[0]))
ordered_user_data = dict(ordered_user_data)

response = requests.post(create_user_url, json=ordered_user_data)

if response.status_code == 201:
    print("Usuário criado com sucesso!")
else:
    print(f"Erro ao criar usuário: {response.text}")
    exit()

login_data = user_data

response = requests.post(login_url, json=login_data)

if response.status_code == 200:
    print("Login realizado com sucesso!")
    
    login_response = response.json()
    with open('login_response.json', 'w') as json_file:
        json.dump(login_response, json_file, indent=4)
    
    print("Resposta do login salva em login_response.json")
else:
    print(f"Erro ao fazer login: {response.text}")