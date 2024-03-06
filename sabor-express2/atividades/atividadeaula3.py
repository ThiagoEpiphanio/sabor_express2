#Atividade1
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Thiago', 'Luany', 'Stefany', 'Fran']
anos = [1984, 2024]

#Atividade2
nomes = ['Thiago', 'Luany', 'Stefany', 'Fran']
for nome in nomes:
    print(f'{nome}')

#Atividade3
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

#Atividade4
for i in range (10, 0, -1):
    print (i)

#Atividade5
numero = int(input('Digite um numero: '))    
for i in range (1,11,1):
    resultado = numero * i
    print (f'{numero} X {i} = {resultado}')

#Atividade6
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#Atividade7
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
