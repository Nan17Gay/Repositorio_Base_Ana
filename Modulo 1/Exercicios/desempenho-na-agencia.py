nome_agente = input('Informe o nome do agente:')
pontualidade = float(input('Informe a nota de pontualidade do agente: '))
produtividade = float(input('Informe a nota de produtividade do agente: '))
colaboracao = float(input('Informe a nota de colaboração de equipe do agente: '))
nota_final = (pontualidade + produtividade + colaboracao) / 30 * 10

classificacao = ''  # variável para guardar a classificação

if nota_final < 0:
    classificacao = 'Nota inválida ❌'
elif nota_final <= 2.9:
    classificacao = 'Crítico 🚨'
    print('Atenção: Sua nota está abaixo do esperado. É importante melhorar seu desempenho em pontualidade, produtividade e colaboração para alcançar melhores resultados.')
elif nota_final <= 4.9:
    classificacao = 'Ruim 🚫'
elif nota_final <= 6.9:
    classificacao = 'Regular ⚠️'
elif nota_final <= 8.9:
    classificacao = 'Bom 👍'
elif nota_final <= 10.0:
    classificacao = 'Excelente 🏅'
    print('Parabéns! Você está se destacando com um desempenho excelente! Continue assim e mantenha seu alto nível de pontualidade, produtividade e colaboração.')
else:
    classificacao = 'Nota inválida ❌'

print('\n===== RELATÓRIO FINAL =====')
print(f'Agente: {nome_agente}')
print(f'Nota Final: {nota_final}')
print(f'Classificação: {classificacao}')