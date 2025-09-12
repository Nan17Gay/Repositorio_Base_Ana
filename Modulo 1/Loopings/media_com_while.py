#Média com while
# 'nota_total' é o acumulador de notas
nome_aluno = input('Informe o nome do aluno: ')

nota_total = 0
bimestre = 0

while bimestre < 4:
    nota = float(input('Digite a nota do aluno: '))
    nota_total += nota #Acumulando a nota total
    bimestre += 1
    print(f'A {nota} digitada do aluno foi armazenada com sucesso!')

media = nota_total / 4 #Calculando a média após sair do loop
print(f'A média do aluno é {media}')

classificacao = ''  # variável para guardar a classificação

if media < 5:
    classificacao = 'Nota abaixo da média! Recuperação com risco de retenção!'
    print('Nota abaixo da média! Recuperação com risco de retenção!')
elif media == 5:
    classificacao = 'Nota média! Leve risco de recuperação sem retenção!'
    print('Nota média! Leve risco de recuperação sem retenção!')
elif media <= 9:
    classificacao = 'Nota acima da média! Sem risco de retenção!'
    print('Nota acima da média! Sem risco de retenção!')
else:
    classificacao = 'Nota máxima! Zero risco de retenção! Parabéns!'
    print('Nota máxima! Zero risco de retenção! Parabéns!')

print('\n===== BOLETIM =====')
print(f'Aluno: {nome_aluno}')
print(f'Nota Final: {media}')
print(f'{classificacao}')