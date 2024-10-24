import random
import os

# declarar variaveis globais

jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1 computador, 2 jogador
maxJogadas = 9


#Matriz

Velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]

]
#funcao para gerenciar a tela


def tela():
    Velha
    os.system("cls")
    print("  0   1   2")
    print("0 " + Velha[0][0] + " | " + Velha[0][1] + " | " + Velha[0][2])
    print("---------------")
    print("1 " + Velha[1][0] + " | " + Velha[1][1] + " | " + Velha[1][2])
    print("---------------")
    print("2 " + Velha[2][0] + " | " + Velha[2][1] + " | " + Velha[2][2])
    print("Jogadas: " + str(jogadas))


# Função para verificar vitória
def verificar_vitoria():
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if Velha[i][0] == Velha[i][1] == Velha[i][2] != " " or \
           Velha[0][i] == Velha[1][i] == Velha[2][i] != " ":
            return Velha[i][0] if Velha[i][0] != " " else Velha[0][i]
    if Velha[0][0] == Velha[1][1] == Velha[2][2] != " " or \
       Velha[0][2] == Velha[1][1] == Velha[2][0] != " ":
        return Velha[1][1]
    return None

#funcoes

def JogadorJoga():
    jogadas
    quemJoga
    maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        try:
            l=int(input("Linha...:"))
            c=int(input("Coluna...:"))
            while Velha[l][c] != " ":
                l = int(input("Linha...:"))
                c = int(input("Coluna...:"))
            Velha[l][c] = "x"
            quemJoga = 1
            jogadas += 1
        
        except:
            print("Linha ou coluna inválida")

def cpuJoga():
    jogadas
    quemJoga
    maxJogadas
    if quemJoga==1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while Velha[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        Velha[l][c] = "0"
        jogadas+=1
        quemJoga=2


while True:
    tela()
    vencedor = verificar_vitoria()
    if vencedor:
        print(f"Jogador {vencedor} venceu!")
        break
    if jogadas >= maxJogadas:
        print("Empate!")
        break
    if quemJoga == 2:
        JogadorJoga()
    else:
        cpuJoga()