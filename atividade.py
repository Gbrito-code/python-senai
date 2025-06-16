valor1 = int(input("Digite um número para treinar a tabuada: "))
valor2 = 1
valor2 = 1
resp = 0
resp_cor = 0
resp_incor = 0
pergunta = ""
aa = 0
while aa == 0:
    if valor2 == 11:
        valor1 = int(input("Digite um número para treinar a tabuada: "))
        valor2 = 1
    resp = int(input(f"Quanto é {valor1} X {valor2}?: "))
    if resp == valor1 * valor2:
        print("Resposta correta!")
        resp_cor += 1
    else:
        print("Resposta incorreta, que pena😥")
        resp_incor += 1
    valor2 += 1
    if valor2 == 11:
        print(f"Parabéns você acertou {resp_cor} e errou {resp_incor}!")
        pergunta = (input("Voce quer continuar? (Sim ou Não)")).lower()
        if pergunta == "sim":
            resp_cor = 0
            resp_incor = 0
            continue
        else:
            break