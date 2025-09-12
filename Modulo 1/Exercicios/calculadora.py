print("Calculadora Simples")

try:
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("Operação inválida.")
    print("Resultado:", resultado)
          
except ValueError:
    print("Erro: você digitou um valor que não é número.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except Exception as e:
    print("Ocorreu um erro inesperado:", e)