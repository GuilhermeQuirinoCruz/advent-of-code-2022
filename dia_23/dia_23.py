class Elfo:
    def __init__(self, posicao):
        self.posicao = posicao
        self.intencao_movimento = [0, 0]

# arquivo_elfos = open("dia_23_exemplo.txt", "r")
# arquivo_elfos = open("dia_23_exemplo2.txt", "r")
arquivo_elfos = open("dia_23_input.txt", "r")
dados_elfos = arquivo_elfos.read().split("\n")
arquivo_elfos.close()

elfos = []
posicoes_ocupadas = []
for y in range(len(dados_elfos)):
    for x in range(len(dados_elfos[y])):
        if dados_elfos[y][x] == "#":
            elfos.append(Elfo([x, y]))
            posicoes_ocupadas.append(tuple([x, y]))

posicoes_ocupadas = set(posicoes_ocupadas)

indice_direcao = 0
direcoes_propor = (((0, -1), [(-1, -1), (0, -1), (1, -1)]),
    ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
    ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
    ((1, 0), [(1, -1), (1, 0), (1, 1)]))

def desenhar_elfos():
    for y in range(-2, 10):
        linha = ""
        for x in range(-3, 11):
            linha += "#" if tuple([x, y]) in posicoes_ocupadas else "."
        print(linha)
    print("")

rounds = 0
limite = 1000
elfo_moveu = True
rounds_sem_mover = 0
# while rounds_sem_mover < 4:
while rounds_sem_mover < 10:
    rounds += 1
    print(f"-Round {rounds}-")
    # primeira metade do round
    posicoes_propostas = []
    for elfo in elfos:
        # print(f"Elfo: {elfo.posicao}")
        elfos_adjacentes = 0
        direcao = [0, 0]
        for i in range(4):
            indice = (indice_direcao + i) % 4
            # print(f"Verificando: {direcoes_propor[indice][0]}")
            direcao_livre = True
            for direcao_propor in direcoes_propor[indice][1]:
                posicao_propor = [elfo.posicao[0] + direcao_propor[0], elfo.posicao[1] + direcao_propor[1]]
                # print(f"Propondo posição: {posicao_propor}")
                if tuple(posicao_propor) in posicoes_ocupadas:
                    # print("Ocupada")
                    direcao_livre = False
                    elfos_adjacentes += 1
            
            if direcao_livre and direcao == [0, 0]:
                # print(f"Direção encontrada: {direcoes_propor[indice][0]}")
                direcao = direcoes_propor[indice][0]
        
        if elfos_adjacentes == 0:
            continue
        
        if direcao != [0, 0]:
            intencao = [elfo.posicao[0] + direcao[0], elfo.posicao[1] + direcao[1]]
            posicoes_propostas.append(intencao)
            elfo.intencao_movimento = intencao
    
    # print(f"Propostas: {posicoes_propostas}")

    # segunda metade do round
    elfo_moveu = False
    novas_posicoes = []
    for elfo in elfos:
        if elfo.intencao_movimento != [0, 0] and posicoes_propostas.count(elfo.intencao_movimento) == 1:
            elfo.posicao = list(elfo.intencao_movimento)
            elfo_moveu = True
        
        elfo.intencao_movimento = [0, 0]
        novas_posicoes.append(tuple(elfo.posicao))
    
    posicoes_ocupadas = set(novas_posicoes)
    indice_direcao = (indice_direcao + 1) % 4

    rounds_sem_mover = 0 if elfo_moveu else (rounds_sem_mover + 1)
    print(len(posicoes_propostas))
    # print(f"Rounds sem movimento: {rounds_sem_mover}")
    # desenhar_elfos()

# PARTE 1
# limites_x = [10000, -10000]
# limites_y = [10000, -10000]
# for elfo in elfos:
#     limites_x[0] = min(limites_x[0], elfo.posicao[0])
#     limites_x[1] = max(limites_x[1], elfo.posicao[0])

#     limites_y[0] = min(limites_y[0], elfo.posicao[1])
#     limites_y[1] = max(limites_y[1], elfo.posicao[1])

# tamanho_x = (limites_x[1] - limites_x[0]) + 1
# tamanho_y = (limites_y[1] - limites_y[0]) + 1
# espacos_vazios = (tamanho_x * tamanho_y) - len(elfos)

# desenhar_elfos()
print(f"Quantidade de elfos: {len(elfos)}")
# print(f"Espaços vazios: {espacos_vazios}")

# PARTE 2
# print(f"Primeiro round sem movimento: {rounds - 3}")
print(f"Primeiro round sem movimento: {rounds - 9}")
# 955 baixo
# 1000 alto