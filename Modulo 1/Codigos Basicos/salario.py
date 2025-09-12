#definir o nome do vendedor
nome = input ('Digite o nome do vendedor:')
print(nome)
#definir salario do vendedor
salario = float(input ('Digite o salario do vendedor:'))
print(salario)
#definir total de vendas efetuadas
vendas = float(input('Digite valor do total de vendas:')) 
print(vendas)
#definir calculo de comissão
comissao = vendas * 0.15
print(comissao)
#definir valor total
total = salario + comissao 
print(total)