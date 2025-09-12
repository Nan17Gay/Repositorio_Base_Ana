nomes = ["Joaquim", "Maria", "Ana"]

print(nomes[0])  # Acessa o primeiro elemento da lista
print(nomes[1])  # Acessa o segundo elemento da lista
print(nomes[2])  # Acessa o terceiro elemento da lista

nomes[0] = "João"

print(nomes[0])  # Acessa o primeiro elemento da lista
print(nomes[1])  # Acessa o segundo elemento da lista
print(nomes[2])  # Acessa o terceiro elemento da lista
print(nomes)

nomes.append("Jonas")
nomes.append("Joana")
print(nomes)

nomes.insert(1, "Fernanda") # Insere "Fernanda" na posição 1
print("Após insert:", nomes)

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no índice 2
print("Após modificação:", nomes)

# Removendo elementos
del nomes[3] # Remove o elemento do índice 3
print("Após del:", nomes)

nomes.remove("Paulo") # Remove a primeira ocorrência de "Paulo"
print("Após remove:", nomes)

removido = nomes.pop(2) # Remove e retorna o elemento no índice 2
print(f"Após pop(removido '{removido}'):", nomes)

nomes.clear() # Esvazia a lista
print("Após clear:", nomes)