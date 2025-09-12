print("Conversor de Moeda - Real para Dólar")

try:
    valor_real = float(input("Digite o valor em reais (R$): "))
    cotacao_dolar = float(input("Digite a cotação atual do dólar: "))

    if cotacao_dolar <= 0:
        raise ValueError("A cotação deve ser maior que zero.")
    
    valor_dolar = valor_real / cotacao_dolar
    print(f"Com R$ {valor_real:.2f} você pode comprar US$ {valor_dolar:.2f}")

except ValueError as ve:
    print("Erro de valor:", ve)
except Exception as e:
    print("Erro inesperado:", e)
