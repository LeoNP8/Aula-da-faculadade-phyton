#Exercício 1
nome = input("qual seu nome?") 
nota1 = float (input("qual á sua primeira nota"))
nota2 = float (input("qual á sua primeira nota"))

print(nome,"sua nota é:")
print((nota1 + nota2)/2)

#Exercício 2
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

print("Nome: ", nome)
print("idade: ", idade)

#Exercício 3

a = 10
b = 20
c = 30
total = (a+b)*c
print(total)

d = 2
e = 42
f = 30
total = (d-e)/f
print(total)

def bomba():
    g = 3
    h = 94
    i = 2
    j = 6
    k = 1
    total = g-(h+i)*6-k
    print(total)

bomba()

x = 6
print(x)
x = x + 1
print(x)

num = int(input("Digite um número com três digitos:"))
d1 = num // 100
d2 = num % 100 // 10
d3 = num % 10
inverso = d3*100+d2*10+d1
print(d1)
print (inverso)

import math

num = float(input("Digite um número"))
resultado = math.sqrt(num)
print("O valor da raiz quadrada é:", resultado)

import math
num = float(input("Digite um número real: "))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(absoluto)
fatorial = math.factorial(math.fabs(inteiro))

print("Absoluto:", absoluto)
print("Inteiro:",inteiro)
print("Raíz:", raiz)
print("Fatorial", inteiro)

a = 33
b = 200

if b > a:
    print("b é maior que a")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c= int(input("Digite o valor de c: "))

if a > b  and c > b:
    print("O menor valor é o b")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200 
b = 33
if b > a:
    print("b é maior que a")
elif a==b:
    print("a e b são iguais")
else:
    print("a é maior que b")

def exercício5_4():
    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both conditions are true")
        