#Exemplos
nome = input("Digite seu nome")
print("Boa noite", nome)

idade = 18
ano = 2006

print(idade)
print(ano)

altura = 1.80
peso = 73.55

print(peso)
print(altura)

a = 5+2j
b = 20+6j
print(a)
print(b)
print(2, 5)

nome = 'Guilherme'
profissao = 'Engenheiro de Software'
print(profissao)
print(nome)

fim_de_semana = True
feriado = False
print(fim_de_semana)
print(feriado)

alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0]
print(alunos)
print(notas)

x = (3)
y = (30)
z = (35)
print(x)
print(y)
print(z)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print("Sejam bem vindos ao mundo da programação")
resposta = input("Digite o seu nome: ")
print("Você digitou: ", resposta)

#nome = input("Digite seu nome: ")
#x = nome.split()
#vetor = list(x)
#print ("Boa noite ", vetor)

quantidade = int(input('Digite a quantidade de produtos a ser cadastrada: '))
vetor = []
for i in range(quantidade):
    produtos = input(f'Digite o nome do {i + 1}º produto: ')
    vetor.append(produtos)
print(f'Produtos cadastrados: {vetor}')

#Exercícios
print("Ciências da Computação - Unicsul")

profissao = input("digite sua profissão")
print("sua profissão é:",profissao)

idade = input("qual o sua idade?")
print("então você tem", idade)

sobrenome = input("qual é seu ultimo sobrenome?")
print("então você é da familia", sobrenome)

esport = input("qual o seu esport favorito?")
print("seu esport favorito é:", esport)