# arquivo_estrategia = open("dia_2_exemplo.txt", "r")
arquivo_estrategia = open("dia_2_input.txt", "r")
dados_estrategia = arquivo_estrategia.read()
lista_estrategia = dados_estrategia.split("\n")
arquivo_estrategia.close()

dict_pontuacao_escolha = {"X" : 1, "Y": 2, "Z" : 3}
# armazena o resultado de cada possibilidade de uma rodada
dict_pontuacao_rodada = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3
}

# PARTE 1
pontuacao = 0

# soma a pontuação da minha escolha e do resultado da rodada
for rodada in lista_estrategia:
    minha_escolha = rodada[-1]

    pontuacao += dict_pontuacao_escolha.get(minha_escolha)
    pontuacao += dict_pontuacao_rodada.get(rodada)

print(pontuacao)

# PARTE 2
pontuacao = 0
possiveis_escolhas = ["X", "Y", "Z"]
escolhas_oponente = ["A", "B", "C"]

# escolhe a forma baseado na escolha do oponente e no resultado esperado
def escolher_forma(rodada):
    indice_escolha = escolhas_oponente.index(rodada[0])
    if rodada[-1] == "X":
        indice_escolha += 2
    elif rodada[-1] == "Z":
        indice_escolha -= 2
    
    # evita que o índice ultrapasse os limites da lista
    indice_escolha = indice_escolha % 3

    return possiveis_escolhas[indice_escolha]

for rodada in lista_estrategia:
    minha_escolha = escolher_forma(rodada)

    rodada_corrigida = rodada[0] + " " + minha_escolha

    pontuacao += dict_pontuacao_escolha.get(minha_escolha)
    pontuacao += dict_pontuacao_rodada.get(rodada_corrigida)

print(pontuacao)