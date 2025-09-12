#Informando distancia e combustivel
distancia = float (input('Informe a distância percorrida: '))
litros = float(input('Informe a quantidade de litros: '))

#Calculo do consumo médio
consumo_medio = distancia / litros
print(f'{distancia} km')
print(f'{litros} l')
print(f'{consumo_medio} km/l')


if consumo_medio < 8:
    print("Menor que 8, Alto consumo!")
    print("Recomenda-se revisar o motor ou calibrar os pneus")
elif 8 > consumo_medio < 12:
    print("Maior que 8 e menor que 12, Consumo moderado!")
else:
    print("Maior ou igual a 12, Ecônomico!")
