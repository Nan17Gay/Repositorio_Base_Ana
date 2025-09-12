print("Tabuada de 1 a 10")

try:
    numero = int(input("Digite um número inteiro para ver a tabuada: "))
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

except ValueError:
    print("Erro: você deve digitar um número inteiro.")
except Exception as e:
    print("Erro inesperado:", e)