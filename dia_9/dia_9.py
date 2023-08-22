import math

# arquivo_movimentos = open("dia_9_exemplo.txt", "r")
# arquivo_movimentos = open("dia_9_exemplo2.txt", "r")
arquivo_movimentos = open("dia_9_input.txt", "r")
dados_movimentos = arquivo_movimentos.read()
lista_movimentos = dados_movimentos.split("\n")
arquivo_movimentos.close()

coordenadas_direcao = {"U" : (0, 1), "D" : (0, -1), "R" : (1, 0), "L" : (-1, 0)}

def distancia_posicoes(p1, p2):
    distancia_x = abs(p2[0] - p1[0])
    distancia_y = abs(p2[1] - p1[1])

    return int(math.sqrt(distancia_x**2 + distancia_y**2))

def direcao_no(no1, no2):
    direcao = [no2[0] - no1[0], no2[1] - no1[1]]

    if abs(direcao[0]) != 0:
        direcao[0] = int(direcao[0] / abs(direcao[0]))
    if abs(direcao[1]) != 0:
        direcao[1] = int(direcao[1] / abs(direcao[1]))
    
    return direcao

def mover_no(no, direcao):
    no[0] += direcao[0]
    no[1] += direcao[1]

def simular_movimentos_corda(qtd_nos, lista_movimentos):
    nos = []
    for i in range(qtd_nos):
        novo_no = [0, 0]
        nos.append(novo_no)
    
    posicoes_visitadas = set()
    
    for movimento in lista_movimentos:
        movimento = movimento.split(" ")
        direcao = coordenadas_direcao.get(movimento[0])
        distancia = int(movimento[1])

        for qtd_movimentos in range(distancia):
            mover_no(nos[0], direcao)

            for i in range(1, len(nos)):
                if distancia_posicoes(nos[i], nos[i - 1]) > 1:
                    mover_no(nos[i], direcao_no(nos[i], nos[i - 1]))
            
            posicoes_visitadas.add(tuple(nos[-1]))
    
    return posicoes_visitadas

# PARTE 1
# posicoes_visitadas_cauda = simular_movimentos_corda(2, lista_movimentos)

# PARTE 2
posicoes_visitadas_cauda = simular_movimentos_corda(10, lista_movimentos)

print("Posições visitadas pela cauda:")
print(posicoes_visitadas_cauda)

print("Quantidade de posições visitadas ao menos uma vez:")
print(len(posicoes_visitadas_cauda))