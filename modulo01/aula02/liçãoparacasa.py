#Tupla
frutas = ('Maça', 'Banana', 'Melão', 'Abacaxi', 'Abacate')
print("Tupla inicial:", frutas)
#Lista
lista = list(frutas)
print("Lista após conversão da tupla:",lista)
#Insira 2 dados extras a essa lista
lista.append('Manga')
lista.append('Maracuja')
print("Lista após adicionar 2 dados:", lista)
#Remova o primeiro dado da lista
lista.pop(0)
print("Lista após remover o primeiro dado:", lista)
#Remova o último dado da lista
lista.pop(-1)
print("Lista após remover o último dado:", lista)
#Faça um print com o primeiro dado da lista
print("Primeiro dado da lista:", lista[0])
#Faça um print com a quantidade de dados da lista
print("Quantidade de dados na lista:", len(lista))
#Crie um dicionário com os seguintes dados:
#Nome, Idade, Profissão
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
profissao = input("Digite a profissão: ")

dicionario = {
    "Nome": nome,
    "Idade": idade,
    "Profissão": profissao
}
print("Valor da chave 'Nome' no dicionário:", dicionario["Nome"])