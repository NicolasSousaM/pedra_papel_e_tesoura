#pedra papel e tesoura
import random
from time import sleep
pontos_do_jogador = 0
pontos_da_maquina = 0

lista = ["pedra", "papel", "tesoura"]
print("\nBem vindo ao pedra papel e tesoura! \nMelhor de Três! Quem fizer dois pontos primeiro ganha!")
while True:
    opcao = int(input("Digite: \n 1 (PEDRA) \n 2 (PAPEL) \n 3 (TESOURA) \n : "))
    jogador = ""
    maquina = random.choice(lista)
    if opcao == 1:
        jogador = "pedra"
    elif opcao == 2:
        jogador = "papel"
    elif opcao == 3:
        jogador = "tesoura"
    else:
        print("Essa não é uma opção válida")
        exit()
    print("***************")
    sleep(1)
    print("PEDRA")
    sleep(1)
    print("PAPEL")
    sleep(1)
    print("TESOURA")
    print("***************")
    sleep(1)
    print(jogador, "(VOCÊ) X", maquina, "(MÁQUINA)")
    if jogador == "pedra" and maquina == "papel":
        print("A MÁQUINA GANHOU")
        pontos_da_maquina += 1
        print("***************")
        sleep(4)
    elif jogador == "pedra" and maquina == "tesoura":
        print("VOCÊ GANHOU")
        pontos_do_jogador += 1
        print("***************")
        sleep(4)
    elif jogador == "papel" and maquina == "pedra":
        print("VOCÊ GANHOU")
        pontos_do_jogador += 1
        print("***************")
        sleep(4)
    elif jogador == "papel" and maquina == "tesoura":
        print("A MÁQUINA GANHOU")
        pontos_da_maquina += 1
        print("***************")
        sleep(4)
    elif jogador == "tesoura" and maquina == "pedra":
        print("A MÁQUINA GANHOU")
        pontos_da_maquina += 1
        print("***************")
        sleep(4)
    elif jogador == "tesoura" and maquina == "papel":
        print("VOCÊ GANHOU")
        pontos_do_jogador += 1
        print("***************")
        sleep(4)
    else:
        print("EMPATE")
        print("***************")
        sleep(4)
    if pontos_do_jogador == 2 or pontos_da_maquina == 2:
        print("***************")
        break
if pontos_do_jogador == 2:
    print("Parabéns! Você ganhou!")
else:
    print("Você Perdeu!")
    