class No:
    def __init__(self, altura, inicio, fim, coord, letra):
        self.altura = altura
        self.vizinhos = []
        self.inicio = inicio
        self.fim = fim
        
        self.letra = letra
        self.coordenadas = coord

def altura_letra(letra):
    if letra == "S":
        return 1
    elif letra == "E":
        return 26
    
    return ord(letra) - 96

# arquivo_alturas = open("dia_12_exemplo.txt", "r")
arquivo_alturas = open("dia_12_input.txt", "r")
dados_alturas = arquivo_alturas.read()
matriz_alturas = dados_alturas.split("\n")
arquivo_alturas.close()

matriz_nos = []
no_inicial = None
no_destino = None

nos_altura_1 = []
for coluna in range(len(matriz_alturas[0])):
    coluna_nos = []
    for linha in range(len(matriz_alturas)):
        letra = matriz_alturas[linha][coluna]
        novo_no = No(altura_letra(letra), letra == "S", letra == "E", [coluna, linha], letra)
        
        coluna_nos.append(novo_no)
        
        if letra == "S":
            no_inicial = novo_no
        elif letra == "E":
            no_destino = novo_no
        elif letra == "a":
            nos_altura_1.append(novo_no)
    
    matriz_nos.append(coluna_nos)

def limites_matriz(x, y):
    limite_x = x >= 0 and x < len(matriz_nos)
    limite_y = y >= 0 and y < len(matriz_nos[0])

    return limite_x and limite_y

def vizinhos_no(x_no, y_no):
    vizinhos = []
    direcoes = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for direcao in direcoes:
        x = x_no + direcao[0]
        y = y_no + direcao[1]
        if limites_matriz(x, y):
            diferenca_altura = matriz_nos[x_no][y_no].altura - matriz_nos[x][y].altura
            if diferenca_altura >= (-1):
                vizinhos.append(matriz_nos[x][y])
    
    return vizinhos

for x in range(len(matriz_nos)):
    for y in range(len(matriz_nos[x])):
        matriz_nos[x][y].vizinhos.extend(vizinhos_no(x, y))

        # print(f"x: {x}, y: {y}")
        # print(len(matriz_nos[x][y].nos_vizinhos))

# PARTE 1
def menor_distancia_destino(inicio):
    nos_visitados = set()
    proximo_conjunto_nos = [inicio]
    numero_passos = -1

    distancia_maxima = len(matriz_nos) * len(matriz_nos[0])

    while len(proximo_conjunto_nos) > 0 and numero_passos < distancia_maxima:
        numero_passos += 1
        nos_visitar = list(proximo_conjunto_nos)

        proximos_nos = []
        for no in nos_visitar:
            nos_visitados.add(no)

            if no == no_destino:
                return numero_passos
            
            for vizinho in no.vizinhos:
                if not vizinho in proximos_nos and not vizinho in nos_visitados:
                    proximos_nos.append(vizinho)
        
        proximo_conjunto_nos = list(proximos_nos)
    
    return distancia_maxima

def menor_caminho(no_inicio, no_fim):
    caminhos = [[no_inicio]]
    indice_caminho = 0
    nos_visitados = set()

    while indice_caminho < len(caminhos):
        caminho_atual = caminhos[indice_caminho]
        ultimo_no = caminho_atual[-1]

        proximos_nos = ultimo_no.vizinhos
        if no_fim in proximos_nos:
            caminho_atual.append(no_fim)
            return caminho_atual
        
        for no in proximos_nos:
            if not no in nos_visitados:
                novo_caminho = caminho_atual[:]
                novo_caminho.append(no)
                caminhos.append(novo_caminho)

                nos_visitados.add(no)
        
        indice_caminho += 1
    
    return []

def imprimir_caminho(caminho):
    nos = []
    for no in caminho:
        nos.append(no.letra)
    
    print(nos)

# caminho = menor_caminho(no_inicial, no_destino)
# imprimir_caminho(caminho)
# print(len(caminho) - 1)

# print("Menor número de passos:")
# print(menor_distancia_destino(no_inicial))

# PARTE 2
contagem = 0
melhor_no = no_inicial
menor_distancia = 10000
for no in nos_altura_1:
    contagem += 1
    # distancia_destino = len(menor_caminho(no, no_destino)) - 1
    distancia_destino = menor_distancia_destino(no)
    if distancia_destino != 0 and distancia_destino < menor_distancia:
        melhor_no = no
        menor_distancia = distancia_destino

print(melhor_no.coordenadas)
print(menor_distancia)