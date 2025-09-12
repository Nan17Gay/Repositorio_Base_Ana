#media com break
nome_aluno = input('Informe o nome do aluno: ')
soma = 0
nota = 0

while True:
    nota = float(input('Digite a nota do aluno: \n ou \nDigite a 99 para SAIR: '))
    if nota == 99:
        break
    soma += nota
print(f'A média do aluno {nome_aluno} é {soma / 4}')