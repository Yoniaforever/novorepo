from faker import Faker

faker = Faker("pt_BR")

Pessoa = {
    "nome": faker.name(),
    "cidade": faker.city(),
    "idade": faker.random_int(18,60)
}

print(Pessoa)