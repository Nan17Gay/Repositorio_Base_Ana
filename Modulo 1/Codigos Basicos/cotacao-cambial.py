# Definição da constante para a taxa de câmbio
DOLAR = 5.50

def traca_linha():
    """
    Imprime uma linha de traços para separar seções do console.
    """
    print("-" * 50)

def converter_para_dolar(valor_em_reais):
    """
    Converte um valor em reais para dólares.
    
    :param valor_em_reais: Valor em reais a ser convertido.
    :return: Valor convertido em dólares.
    """
    return valor_em_reais / DOLAR

def converter_para_reais(valor_em_dolares):
    """
    Converte um valor em dólares para reais.
    
    :param valor_em_dolares: Valor em dólares a ser convertido.
    :return: Valor convertido em reais.
    """
    return valor_em_dolares * DOLAR

def conversor_moeda():
    
    print("Conversor de Moeda | Escolha uma opção:")
    opcao = int(input("1. Converter Reais para Dólares \n2. Converter Dólares para Reais : "))
    traca_linha()

    match opcao:
        case 1:
            print("Converter Reais para Dólares")
            traca_linha()
            valor_em_reais = float(input("Digite o valor em reais: "))
            traca_linha()
            valor_em_dolares = converter_para_dolar(valor_em_reais)
            traca_linha()
            print(f"Valor em dólares: {valor_em_dolares:.2f}")
        case 2:
            valor_em_dolares = float(input("Digite o valor em dólares: "))
            traca_linha()
            valor_em_reais = converter_para_reais(valor_em_dolares)
            traca_linha()
            print(f"Valor em reais: {valor_em_reais:.2f}")
        case _:
            print("Opção inválida. Tente novamente.")
            return

# Executa o conversor de moeda 
conversor_moeda()