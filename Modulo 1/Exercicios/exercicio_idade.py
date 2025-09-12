#Você foi contratado para criar um programa de verificação de idade para clientes que consumem bebida alcoolica

#Passo 1. nome do cliente
nome = input("Digite o seu nome: ")

#Passo 2. idade
idade = int(input('Digite sua idade: '))

#if é SE em pt-br e else é SENÃO
if idade >= 18:
    print(nome, 'Autorizado(a), maior de idade', idade)
else:
    print(f'{nome} Não autorizado(a), menor de idade: {idade} anos')
    