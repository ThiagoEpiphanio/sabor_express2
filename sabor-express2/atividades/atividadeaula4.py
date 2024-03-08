#Atividade1
pessoa = [{'nome': 'Thiago', 'idade': '39', 'cidade': 'Caieiras'}]

#Atividade2
pessoa = [{'nome': 'Thiago', 'idade': '39', 'cidade': 'Caieiras'}]
    #Atualição de idade
pessoa['idade'] = 40
    #Adicionado profissão
pessoa['profissao'] = 'Engenheiro'
    #Remoção de Elemento
del pessoa['cidade']

#Atividade3
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#Atividade4
pessoa2 = [{'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}]
if 'nome' in pessoa2:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#Atividade5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)




