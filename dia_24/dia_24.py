import math

class Neve:
    def __init__(self, posicao, direcao):
        self.posicao = posicao
        self.direcao = direcao

class No:
    def __init__(self, posicao, vizinhos):
        self.posicao = posicao
        self.vizinhos = vizinhos

# arquivo_mapa = open("dia_24_exemplo.txt", "r")
arquivo_mapa = open("dia_24_input.txt", "r")
dados_mapa = arquivo_mapa.read().split("\n")
arquivo_mapa.close()

def direcao_neve(char):
    match(char):
        case ">":
            return tuple([1, 0])
        case "<":
            return tuple([-1, 0])
        case "^":
            return tuple([0, -1])
        case "v":
            return tuple([0, 1])

neves = []
for y in range(1, len(dados_mapa) - 1):
    for x in range(1, len(dados_mapa[0]) - 1):
        if dados_mapa[y][x] == ".":
            continue
        
        neves.append(Neve([x, y], direcao_neve(dados_mapa[y][x])))

largura = len(dados_mapa[0]) - 2
altura = len(dados_mapa) - 2

canto_sup_esq = tuple([1, 1])
canto_inf_dir = tuple([largura, altura])

posicao_inicial = tuple([1, 0])
posicao_final = tuple([len(dados_mapa[0]) - 2, len(dados_mapa) - 1])

def posicoes_mapa():
    posicoes = set()
    for x in range(canto_sup_esq[0], canto_inf_dir[0] + 1):
        for y in range(canto_sup_esq[1], canto_inf_dir[1] + 1):
            posicoes.add(tuple([x, y]))
    
    posicoes.add(posicao_inicial)
    posicoes.add(posicao_final)

    return posicoes

def posicoes_ocupadas():
    posicoes = set()
    for neve in neves:
        posicoes.add(tuple(neve.posicao))
    
    return posicoes

def mover_neve():
    for neve in neves:
        neve.posicao = [neve.posicao[0] + neve.direcao[0], neve.posicao[1] + neve.direcao[1]]
        if neve.posicao[0] > largura:
            neve.posicao[0] = 1
        elif neve.posicao[0] < 1:
            neve.posicao[0] = largura
        
        if neve.posicao[1] > altura:
            neve.posicao[1] = 1
        elif neve.posicao[1] < 1:
            neve.posicao[1] = altura

tempo_posicao = {}
posicoes_vazias = set()
minuto_repetir = math.lcm(altura, largura)
posicoes_validas = posicoes_mapa()
nos_tempo = {}
for minuto in range(minuto_repetir):
    posicoes_vazias = posicoes_validas.difference(posicoes_ocupadas())
    posicoes_minuto = set()
    for posicao in posicoes_vazias:
        posicoes_minuto.add(tuple([posicao[0], posicao[1], minuto]))
    tempo_posicao[minuto] = posicoes_minuto
    mover_neve()

    nos_tempo[minuto] = set()

def posicoes_iguais(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

def posicao_valida(posicao):
    if posicoes_iguais(posicao, posicao_inicial) or posicoes_iguais(posicao, posicao_final):
        return True

    x_valido = posicao[0] > 0 and posicao[0] <= largura
    y_valido = posicao[1] > 0 and posicao[1] <= altura

    return x_valido and y_valido

def adjacentes_validos(posicao):
    direcoes = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    adjacentes = []
    for i in range(5):
        adjacente = [posicao[0] + direcoes[i][0], posicao[1] + direcoes[i][1], (posicao[2] + 1) % minuto_repetir]
        if posicao_valida(adjacente):
            adjacentes.append(tuple(adjacente))
    
    return adjacentes

nos = []
nos_iniciais = set()
no_ida = None
nos_finais = set()
for minuto in range(minuto_repetir):
    posicoes_proximo_minuto = tempo_posicao[(minuto + 1) % minuto_repetir]
    for posicao in tempo_posicao[minuto]:
        adjacentes = adjacentes_validos(posicao)
        adjacentes_proximo_minuto = []
        for adjacente in adjacentes:
            if adjacente in posicoes_proximo_minuto:
                adjacentes_proximo_minuto.append(adjacente)
        
        novo_no = No(posicao, adjacentes_proximo_minuto)
        nos.append(novo_no)
        nos_tempo[minuto].add(novo_no)

        if posicoes_iguais(posicao, posicao_inicial):
            nos_iniciais.add(novo_no)
            if minuto == 0:
                no_ida = novo_no
        
        if posicoes_iguais(posicao, posicao_final):
            nos_finais.add(novo_no)

for no in nos:
    if len(no.vizinhos) == 0:
        continue
    
    nos_vizinhos = []
    for possivel_vizinho in nos_tempo[(no.posicao[2] + 1) % minuto_repetir]:
        if possivel_vizinho.posicao in no.vizinhos:
            nos_vizinhos.append(possivel_vizinho)
    
    no.vizinhos = nos_vizinhos

def menor_caminho(no_inicio, nos_destino):
    caminhos = [[no_inicio]]
    indice_caminho = 0
    nos_visitados = set()

    while indice_caminho < len(caminhos):
        caminho_atual = caminhos[indice_caminho]
        ultimo_no = caminho_atual[-1]

        proximos_nos = ultimo_no.vizinhos
        for no in nos_destino:
            if no in proximos_nos:
                caminho_atual.append(no)
                return caminho_atual
        
        for no in proximos_nos:
            if not no in nos_visitados:
                novo_caminho = caminho_atual[:]
                novo_caminho.append(no)
                caminhos.append(novo_caminho)

                nos_visitados.add(no)
        
        indice_caminho += 1
        # print(f"Caminhos avaliados: {indice_caminho}")
    
    return []

# PARTE 1
# caminho = menor_caminho(no_ida, nos_finais)
# print(f"Quantidade mínima de minutos: {len(caminho) - 1}")

# PARTE 2
minutos_totais = 0

caminho = menor_caminho(no_ida, nos_finais)
minutos_totais += (len(caminho) - 1)

no_volta = caminho[-1]
caminho = menor_caminho(no_volta, nos_iniciais)
minutos_totais += (len(caminho) - 1)

no_ida = caminho[-1]
caminho = menor_caminho(no_ida, nos_finais)
minutos_totais += (len(caminho) - 1)
print(f"Tempo total: {minutos_totais}")