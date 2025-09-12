#Monitoramento de Saúde com Cálculo de IMC
nome_paciente = input('Informe o nome do paciente: ')
peso = float(input('Informe o peso do paciente: '))
altura = float(input('Informe a altura do paciente: '))
imc = peso / (altura ** 2)

classificacao = ''  # variável para guardar a classificação


if imc <= 18.5 :
    classificacao = 'Abaixo do peso'
elif imc <= 24.9:
    classificacao = 'Peso normal'
elif imc <=  29.9:
    classificacao = 'Sobrepeso'
elif imc <= 34.9:
    classificacao = 'Obesidade Grau I'
elif imc <= 39.9:
    classificacao = 'Obesidade Grau II'
elif imc >= 40.0:
    classificacao = 'Obesidade Grau III (mórbida)'
else:
    classificacao = 'Error!'

print('\n===== RELATÓRIO FINAL =====')
print(f'Paciente: {nome_paciente}')
print(f'Altura: {altura} m')
print(f'Peso: {peso} kg')
print(f'Valor do IMC: {imc}')
print(f'Classificação: {classificacao}')