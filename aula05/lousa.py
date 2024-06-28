import requests 

cep = input("qual seu cep? ")

response = requests.get (f"https://viacep.com.br/ws/{cep}/json/")

data = response.json()

print ("o logradouro desse local é:", data["logradouro"])
