#Loop For
#Para cada número: Exibe o valor
"""notas = [10, 9, 7, 5, 8]
for numero in notas:
    print(f"Nota: {numero}")

for caractere in "palavra":
    print(caractere)
"""

"""for numero in range(3):
    print(numero)"""

"""#Usando o range (inicio= 0, fim, salto= 1 )
for i in range(0,7,1):
    print("Gol da alemanha!")
    print(i)
print("Gol do Brasil")"""


"""#usando o break com for
for i in range(10000):
    print("Gol da alemanha")
    if i == 6:
        break
print("Gol do Brasil")
"""
"""#Média da sala de aula
qtd_alunos = int(input("Digite a quantidade de aluno na sala: "))
total_notas = 0
for i in range(qtd_alunos): 
    nota = float(input(f"Digite a nota do {i+1}° aluno: "))
    total_notas += nota
print(f"A média da sala é: {total_notas/qtd_alunos:.2f}")

num = int(input("Digite um número: "))
for i in range(1,11):
    print(f" {num} x {i} = {num * i}")
    """
