#Passo 1. nome do cliente
nome_do_cliente = input('Seja bem vindo! Qual o seu nome, por favor?')

#Passo 2. endereço
endereco = input('Endereço de entrega:')

#Passo 3. receber o pedido
pedido = (input("Escolha o sabor da sua pizza \n ( Mussarela | Calabresa | Portuguesa | Marguerita)  "))

#Passo 4. opções
if pedido == "Mussarela":
    print(f"Sr(a) {nome_do_cliente}, o seu pedido será entregue no endereço {endereco}, sabor escolhido: {pedido}.")
elif pedido == "Calabresa":
    print(f"Muito obrigado pelo seu pedido, {nome_do_cliente}. Nosso motoboy já está a caminho do {endereco} com a sua pizza de {pedido}.")
elif pedido == "Portuguesa":
    print(f"Excelente escolha, {nome_do_cliente}. A nossa pizza {pedido} chegará em breve no endereço {endereco}.")
elif pedido == "Marguerita":
    print(f"Oba! A pizza {pedido} chegará quentinha na sua casa, {endereco}. Agradecemos pelo pedido, {nome_do_cliente}!")
else:
    print("Desculpe, sabor inválido. Por favor, escolha uma das opções listadas.")