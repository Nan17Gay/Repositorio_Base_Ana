# -usuario ira inserir dois valores 
#variavel é um espaço reservado  na memoria que recebe dados 
#tipos variaveis ( texto, booleano, numero (inteiro e float( flutuante-peso, altura, medida)))

numero1 = int(input("Insira o primeiro numero:"))
#print(numero1)

numero2 = float(int(input("Insira o segundo numero que seja flutuante:")))
#print(numero2)

#calculo de soma
soma = numero1 + numero2 
print(" o valor de entre os numeros declaradob é :",soma)

#calculo subtração 
subtração = numero1 - numero2 
print("A subtração dos numeros é :", subtração)

#calculo multiplicação 
multiplicação = numero1 * numero2 
print("A multiplicação dos numeros é :",multiplicação)

#calculo potencia 
potencia = numero1 ** numero2 
print("A potencia do numero 1 elevado ao numero 2 é :", potencia)

#exemplo booleano 
idade = int(input("Digite a sua idade:"))
if idade >=18:
    print(True)
else:
    print(False) 