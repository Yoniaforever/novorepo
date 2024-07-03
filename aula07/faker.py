from faker import Faker


faker = Faker("pt_BR")

Pessoa = {
    "nome": faker.name(),
    "cidade": faker.address()
}