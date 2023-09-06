"""Faça um programa em Python do jogo de "pedra, papel, tesoura" com você vs o computador.

Utilize a função random para sortear de uma lista ou dicionário.
Pare o jogo quando o usuário ou a máquina fizer 3 pontos ou, depois 
de 5 rodadas, ninguém tiver feito 3 pontos declare EMPATE! """

import random

lista1 = ["pedra", "papel", "tesoura"]
pts_pc = 0
pts_lau = 0
rodadas = 0

while pts_lau < 3 and pts_pc < 3 and rodadas < 5:
    rodadas +=1
    if rodadas == 5:
        print("empate")
        break
    item_sorteado = random.choice(
        lista1
    )  
    escolha = input("pedra, papel, tesoura: ")
    print(f"O item sorteado foi {item_sorteado}")
   
    if escolha == "pedra":
        if item_sorteado == "tesoura":
            pts_lau += 1
        elif item_sorteado == "papel":
            pts_pc += 1
        else:
            print("Empate")

    elif escolha == "tesoura":
        if item_sorteado == "pedra":
            pts_pc += 1
        elif item_sorteado == "papel":
            pts_lau += 1
        else:
            print("Empate!")

    elif escolha == "papel":
        if item_sorteado == "tesoura":
            pts_pc += 1
        elif item_sorteado == "pedra":
            pts_lau += 1
        else:
            print("Empate!")

    print(f"Placar é Laura: {pts_lau} vs PC: {pts_pc}")
    


def placar():
    if pts_lau == 3:
        print("Laura venceu")
    elif pts_pc == 3:
        print("O pc venceu")


placar() 
