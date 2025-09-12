def celsius_para_fahrenheit():
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit: .2f}°F.")
    except ValueError:
        print("Erro: Por favor, digite um número válido para a temperatura.")

def fahrenheit_para_celsius():
    try:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F é igual a {celsius: .2f}°C.")
    except ValueError:
        print("Erro: Por favor, digite um número válido para a temperatura.")

def main():
    print("Conversor de Temperaturas")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    escolha = input("Escolha a conversão (1 ou 2): ")

    if escolha == "1":
        celsius_para_fahrenheit()
    elif escolha == "2":
        fahrenheit_para_celsius()
    else: 
        print("Opção inválida. Por favor, escolha 1 ou 2.")

# Chamada da função principal
main()