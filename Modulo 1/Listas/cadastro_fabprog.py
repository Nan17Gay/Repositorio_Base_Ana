contatos = []

while True:
    print("\nAGENDA DE CONTATOS - FABPROG")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Excluir contato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        pessoa = [nome, telefone, email]
        contatos.append(pessoa)
        print("Contato cadastrado com sucesso!")

    elif opcao == "2":
        if len(contatos) == 0:
            print("Nenhum contato cadastrado.")
        else:
            print("\nLista de Contatos:")
            indice = 0
            while indice < len(contatos):
                pessoa = contatos[indice]
                print(str(indice + 1) + ". Nome: " + pessoa[0] + ", Telefone: " + pessoa[1] + ", E-mail: " + pessoa[2])
                indice = indice + 1

    elif opcao == "3":
        if len(contatos) == 0:
            print("Nenhum contato para excluir.")
        else:
            print("\nContatos:")
            i = 0
            while i < len(contatos):
                print(str(i + 1) + ". " + contatos[i][0])
                i = i + 1

            num = input("Digite o número do contato que deseja excluir: ")
            if num.isdigit():
                indice = int(num) - 1
                if indice >= 0 and indice < len(contatos):
                    removido = contatos.pop(indice)
                    print("Contato '" + removido[0] + "' excluído com sucesso.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida. Digite um número.")

    elif opcao == "0":
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")