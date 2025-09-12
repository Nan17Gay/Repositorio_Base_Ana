print("Cálculo de IMC (Índice de Massa Corporal)")

try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")

    imc = peso / (altura ** 2)
    print("Seu IMC é:", round(imc, 2))

except ValueError as ve:
    print("Erro de valor:", ve)
except Exception as e:
    print("Erro inesperado:", e)
