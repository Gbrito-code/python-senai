# Loop While
# Enquanto contador for menor ou igual a 5, ele imprime o valor e soma +1
"""
contador = 1
while contador <= 5:
    print(f"Contador está em {contador}")
    contador = contador + 1

gols = 0
while gols < 7:
    gols = gols + 1
    print("Gol da alemanha")
print("Gol da Brasil")

contador = 1
total_soma = 0
while contador <= 5:
    total_soma += 1
    contador += 1
    print(f"A soma total é {total_soma}")
"""
"""#Usando else com while 
x = 0
while x < 5:
    print(f"O valor de x nesta iteração é {x}")
    print(f"x ainda é menor que 5, somando 1 a x")
    print("-" * 50)
    x = x + 1
    #x += 1
else:
    print("Loop concluído!")

senha = ""
while senha != "python123":
    senha = input("Digite sua senha: ")
else: 
    print("Senha correta! Acesso liberado")

valor = int(input("Quanto é 2 + 2: "))
while valor != 4:
    pri0nt("Errouuu")
    valor = int(input("Quanto é 2 + 2: "))
print("Certa resposta!")

# Utilizar o break no while
#Se encontramos o número 4, interrompemos o loop
valor = 0
while valor < 100:
    if valor == 4:
        break
    else: 
        #nenhuma ação específica
        pass
    print(valor)
    valor += 1
"""

"""notas = 0
qtd_notas_info = 0
while True:
    nota = float(input("Informe a nota ou ( -1 para finalizar ): "))
    if nota == -1:
        break
    notas += nota
    qtd_notas_info += 1

if qtd_notas_info > 0: 
    media = notas / qtd_notas_info
    print(f"Quantidade de notas informadas: {qtd_notas_info}")
    print(f"Média da sala: {media:.2f}")
else:
    print("Nenhuma nota informada!")
    Número aleatório
"""
#Crie um programa que peça para o usuário adivinhar 
# um número secreto (o número secreto é 7).
# Enquanto o usuário não acertar, o programa deve dizer
#"Errado, tente novamente.". Quando o usuário acertar, 
# o programa deve dizer "Parabéns, você acertou!".
import random

numero_secreto = random.randint(1,100)
numero = 0
while numero != numero_secreto:
    numero = int(input("Digite o número secreto (entre 1 e 100): "))
    if numero != numero_secreto:
        print("Errado, tente novamente.")
        if numero > numero_secreto:
            print("Tente um número menor")
        else:
            print("Tente um número maior")
print("Parabéns, você acertou!")