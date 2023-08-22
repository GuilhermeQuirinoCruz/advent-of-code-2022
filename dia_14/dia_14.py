arquivo_caverna = open("dia_14_exemplo.txt", "r")
# arquivo_caverna = open("dia_14_input.txt", "r")
dados_caverna = arquivo_caverna.read()
arquivo_caverna.close()

caminhos = []
menor_x = 1000
maior_x = 0
limite_y = 0

for caminho in dados_caverna.split("\n"):
    coordenadas = caminho.replace(" ", "").split("->")
    caminho = []
    for coordenada in coordenadas:
        coordenada = coordenada.split(",")
        x = int(coordenada[0])
        y = int(coordenada[1])

        caminho.append([x, y])

        menor_x = min(menor_x, x)
        maior_x = max(maior_x, x)

        limite_y = max(limite_y, y)
    
    caminhos.append(caminho)

# remapeando as coordenadas baseado no menor valor de x
maior_x -= menor_x
for caminho in caminhos:
    for par_coordenadas in caminho:
        par_coordenadas[0] -= menor_x

matriz_caverna = []
for x in range(maior_x + 1):
    coluna = []
    for y in range(limite_y + 1):
        coluna.append(0)
    
    matriz_caverna.append(coluna)

# preenchendo com as paredes
for caminho in caminhos:
    for i in range(len(caminho) - 1):
        inicio_pedra = caminho[i]
        fim_pedra = caminho[i + 1]

        numero_pedras = max(abs(fim_pedra[0] - inicio_pedra[0]), abs(fim_pedra[1] - inicio_pedra[1])) + 1
        x = None
        if inicio_pedra[0] == fim_pedra[0]:
            x = [inicio_pedra[0]] * numero_pedras
        else:
            direcao = 1 if inicio_pedra[0] < fim_pedra[0] else -1
            x = list(range(inicio_pedra[0], fim_pedra[0] + direcao, direcao))
        
        y = None
        if inicio_pedra[1] == fim_pedra[1]:
            y = [inicio_pedra[1]] * numero_pedras
        else:
            direcao = 1 if inicio_pedra[1] < fim_pedra[1] else -1
            y = list(range(inicio_pedra[1], fim_pedra[1] + direcao, direcao))

        for i in range(numero_pedras):
            matriz_caverna[x[i]][y[i]] = -1

x_inicial_areia = 500 - menor_x

def imprimir_matriz_caverna():
    desenho = ""
    for y in range(len(matriz_caverna[0])):
        for x in range(len(matriz_caverna)):
            char = ""
            match(matriz_caverna[x][y]):
                case 0:
                    char = "."
                case 1:
                    char = "o"
                case -1:
                    char = "#"

            if x == x_inicial_areia and y == 0 and not posicao_ocupada(x, y):
                char = "+"
            
            desenho += char
        desenho += "\n"
    
    print(desenho)

def posicao_valida(x, y):
    x_valido = x >= 0 and x <= maior_x
    y_valido = y >= 0 and y <= limite_y

    return x_valido and y_valido

def posicao_ocupada(x, y):
    return matriz_caverna[x][y] == -1 or matriz_caverna[x][y] == 1

def simular_unidade_areia():
    posicao = [x_inicial_areia, 0]
    direcoes_possiveis = ((0, 1), (-1, 1), (1, 1))
    direcao = [0, 1]
    repouso = True

    while direcao != [0, 0]:
        if not posicao_valida(posicao[0], posicao[1]):
            repouso = False
            break
        
        direcao = [0, 0]
        for proxima_direcao in direcoes_possiveis:
            proxima_posicao = [posicao[0] + proxima_direcao[0], posicao[1] + proxima_direcao[1]]

            if not posicao_valida(proxima_posicao[0], proxima_posicao[1]):
                repouso = False
                continue

            if not posicao_ocupada(proxima_posicao[0], proxima_posicao[1]):
                direcao = proxima_direcao
                posicao[0] += direcao[0]
                posicao[1] += direcao[1]
                repouso = True
                break
    
    if repouso:
        if not posicao_ocupada(posicao[0], posicao[1]):
            matriz_caverna[posicao[0]][posicao[1]] = 1
        else:
            repouso = False

    return repouso

def remover_areia():
    for y in range(len(matriz_caverna[0])):
        for x in range(len(matriz_caverna)):
            if matriz_caverna[x][y] == 1:
                matriz_caverna[x][y] = 0

# PARTE 1
unidades_areia_simuladas = 0
while simular_unidade_areia():
    unidades_areia_simuladas += 1 

print(f"Unidades de areia simuladas: {unidades_areia_simuladas}")
imprimir_matriz_caverna()

remover_areia()

# PARTE 2
coluna_extra = ([0] * (limite_y + 2)) + [-1]
for coluna in matriz_caverna:
    coluna.extend([0, -1])

limite_y += 2
colunas_adicionar_esquerda = limite_y - x_inicial_areia
colunas_adicionar_direita = limite_y - (maior_x - x_inicial_areia)

for i in range(colunas_adicionar_esquerda):
    matriz_caverna.insert(0, list(coluna_extra))

for i in range(colunas_adicionar_direita):
    matriz_caverna.append(list(coluna_extra))

x_inicial_areia += colunas_adicionar_esquerda
maior_x += colunas_adicionar_esquerda + colunas_adicionar_direita

unidades_areia_simuladas = 0
while simular_unidade_areia():
    unidades_areia_simuladas += 1

imprimir_matriz_caverna()
print(f"Unidades de areia simuladas: {unidades_areia_simuladas}")