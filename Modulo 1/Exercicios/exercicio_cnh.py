#Você foi contratado para criar um programa para uma autoescola, que deve verificar se a pessoa é maior ou tem 18 anos. Se ela tiver 18 ou mais, ela pode ter cnh, senão Não pode dirigir.

#1. Receber o nome da pessoa
nome = input('Digite o seu nome: ')
#2. Receber a idade da pessoa
idade = int(input('Digite a sua idade: '))
#3. possui cnh?
possui_cnh = input("Você possui a carteira de habilitação? \n (1- Sim / 2- Não): ")
#4. verificar se a pessoa >= 18
if idade >= 18:
    #5. Se ele já é maior de idade, vou verificar se ele tem ou não a cnh
    if possui_cnh == "1":
        print('Maior de 18 anos e pode dirigir!')
    else:
        print('Não pode dirigir, porque não possui CNH')
else:
    print('Menor de idade')
    