nome_ia = input('Informe o nome da I.A.: ')
pontuacao = float(input('Informe a pontuação: '))

classificacao = ''  # variável para guardar a classificação

if pontuacao < 0:
    classificacao = ('Erro: Pontuação inválida!')
elif pontuacao <= 39.9:
    classificacao = ('IA em treinamento🍼')
    print('🔁 Continue alimentando os dados para melhorar a performance.')
elif 40.0 > pontuacao < 69.9:
    classificacao = ('IA Intermediária 🧠')
elif 70.0 > pontuacao < 89.9:
    classificacao = ('IA Otimizada 🚀')
elif 90.0 > pontuacao < 100.0:
    classificacao = ('IA Avançada (nível Skynet) 🤯')
    print('⚡ Iniciando protocolo de expansão neural...')
else:
    classificacao = ('Erro: IA fora da escala!')

print('\n===== RELATÓRIO FINAL =====')
print(f'Sistema: {nome_ia}')
print(f'Pontuação: {pontuacao}')
print(f'Classificação: {classificacao}')