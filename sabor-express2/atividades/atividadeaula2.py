#Atividade1
numero = int(input('Digite um número: '))

if numero %2 == 0:
    print ('O número é par\n')
else:
    print ('O número é ímpar\n')

#Atividade2
idade = int(input('Digite a sua idade: '))
if 0< idade <= 12:
    print ('Criança\n')
elif 12 < idade <=18:
    print ('Adolescente\n')
elif idade > 18:
    print("Adulto\n")
else:
    print ('Valor inválido')


#Atividade3
nome = input('Digite o seu nome: ')
senha = int(input('Digite a sua senha: '))
if nome == 'Thiago' and senha == 1234:
    print ('Nome e senha estão corretos')
else:
    print ('Nome e senha incorretos')

#Atividade4
x = int(input('Digite as coordenadas do ponto X: '))
y = int(input('Digite as coordenadas do ponto Y: '))
print('')

if x>0 and y>0:
    print('Primeiro Quadrante')
elif x<0 and y>0:
    print('Segundo Quadrante')
elif x<0 and y<0:
    print('Terceiro Quadrante')
elif x>0 and y<0:
    print('Quarto Quadrante')
else:
    print('O ponto está localizado no eixo ou origem')