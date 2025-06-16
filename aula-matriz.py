# Trabalhando com matriz
# Matriz = lista dentro de lista

# print(matriz[0])
# print(matriz[0][2])


#Percorrendo matriz com for
# for linha in matriz:
#     print(linha)
#     for valor in linha:
#         print(valor)
#     print()

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]  
# ]
# #Percorrendo a matriz com range()
# print(len(matriz))
# print("Elementos da matriz:")
# for i in range(len(matriz)):
#     print(matriz[i])
#     for j in range(len(matriz[i])):
#         print(f"Elemento [{i}][{j}] = {matriz[i][j]}")

"""alunos = [
    ["Davi", 28, "A"],
    ["Emilly", 32, "C"],
    ["Guilherme", 71, "B"],
    ["Igor", 95, "A"]
]
#Exibir valores da matriz
for aluno in alunos:
    print(f"{aluno[0]:<10} | {aluno[1]:<5} | {aluno[2]}")

#adicionar valores na matriz
nome = input("Digite seu nome: ").capitalize()
idade = int(input("Digite sua idade: "))
turma = input("Digite sua turma: ").upper()
alunos.append([nome, idade, turma])

#Exibir valores da matriz
for aluno in alunos:
    print(f"{aluno[0]:<10} | {aluno[1]:<5} | {aluno[2]}") """

#verificar se a lista está vazia.
# #Lista vazia é considera como false
# alunos = []

# if not alunos:
#     print("A lista está vazia")

# alunos.append("Gabriel")

# if not alunos:
#     print("A lista está vazia")
# else:
#     print("Temos alunos cadastrado! ")


# Criar uma matriz 3x3 com valores fornecidos pelo usuário
matriz = []

print("Preencha a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = input(f"Digite o valor para posição [{i}][{j}]: ")
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)