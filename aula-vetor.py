#Estrutura de dados (lista / vetor)
# Criando uma lista/vetor
"""# índice          0             1         2
bancos = ["Banco do Brasil", "Caixa", "Santader" ]
#                -3            -2        -1
#Acessando os elementos da lista
print( bancos[-2] )
print(type(bancos))
#Alterando os valores da lista/vetor
bancos[1] = "Inter"
print(bancos)
#Alterando o ultimo elemento da lista
bancos[-1] = "Nubank"
print(bancos)
#Percorrendo os valores do vetor/lista
for banco in bancos:
    print(banco, end=", ")"""

"""#Percorrendo os valores do vetor com for
cores = ["azul", "verde", "vermelho"]
#len() = pega o total de elementos da lista
for i in range( len(cores) ):
    cor = cores[i]
    print(f"Cor do indice {i} é {cor}")
"""
#Fatiamento com lista/strings
"""numeros = [10, 20, 30, 40, 50, 60]
#Pegar os 3 primeiros elementos da lista?
print(numeros[:3])

#Pegar os 3 ultimos elementos da lista
print(numeros[-2:])

#Pegar do índice 1 até o índice 4
#O ultimo indice não é incluído
print(numeros[1:4])

#Inverter a lista com fatiamento
print(numeros[::-1])"""

"""compras = [10.5, 3.80, 17.2, ["tomate", "sabonete", "arroz"] ]

produtos = compras[3]
print(produtos[1])

#Somar os valores dos itens pelo indice
total = compras[0] + compras[1] + compras[2]
print(total)

#Criando lista 
letras = ["a", "b", "c"]
num = [2, 4, 6]
tudo = [letras, num]
print(tudo[1][1])"""

"""#Verificar a existência de um item na lista
letras = ["a", "b", "c", "d", "e", "f", "g"]
var = input("Digite uma letra para pesquisa: ").lower()
#in procura um valor dentro da lista
if var in letras:
    print(f"A letra {var} está na lista")
else:
    print(f"A letra {var} NÃO está na lista")
"""
"""
#Adicionar alguns elementos fornecidos pelo usuário na lista
lista_tarefas = []

tarefa = input("Digite uma tarefa: ")
lista_tarefas.append(tarefa)
print(lista_tarefas)

while True:
    tarefa = input("Digite uma tarefa ou (0 para sair): ")
    if tarefa == "0":
        break
    else:
        lista_tarefas.append(tarefa)
print(lista_tarefas)"""

#Outras funções com lista

"""numeros = [10, 6, 3, 7, 2]

#max() retorna o maior valor da lista
print(max(numeros))
#min() retorna o menor valor da lista
print(min(numeros))
#sum() soma de todos os itens
print(sum(numeros))"""
"""
#Exemplo pratico 
produtos = ["macbook", "ipad", "apple Watch", "air pods", "iphone 15", "vision pro" ]

#Adicionar um valor na lista
produtos.append(input("Digite um item para adicionar na lista de produtos: "))

#Remover um item
item_removido = input("Digite o produto que deseja remover: ").lower()
if item_removido in produtos:
    produtos.remove(item_removido)
    print("Produto foi removido com sucesso!")
else:
    print(f"{item_removido} não existe na lista de produtos da apple!")

for item in produtos:
    print(f"- {item}")"""

"""
Crie um programa em Python que simule uma lista de compras. 
O programa deve:
Criar uma lista vazia chamada compras.
Pedir ao usuário para digitar 5 itens de compra e adicioná-los à lista usando append.
Mostrar a lista completa com os itens.
Perguntar qual item o usuário deseja substituir (pelo nome) 
e pelo que ele deseja substituir.
Mostrar a nova lista atualizada.
Exibir a lista final com uma mensagem de agradecimento.
"""
#Passo 1 - lista vazia
compras = []

#passo 2 - Adicionar 5 itens
print("\nDigite 5 itens para sua lista de compras:")
for i in range(5):
    item = input(f"Item {i + 1}: ")
    compras.append(item)

#Passo 3 - mostrar a lista de compras
print("\nSua lista de compras:")
for item in compras:
    print(f"- {item}")

#Passo 4 - perguntar quanto item ele quer substituir pelo nome
antigo = input("\nQual item você deseja substituir: ")

if antigo in compras:
    posicao = compras.index(antigo)
    novo_item = input("Digite o novo item: ")
    compras[posicao] = novo_item
else:
    print("Esse item não está na lista de compras")

#Passo 5 - lista atualizada
print("\nSua lista de compras atualizada:")
for item in compras:
    print(f"- {item}")

print("Obrigado pela lista de compras!")