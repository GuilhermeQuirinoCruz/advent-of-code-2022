class Posicao:
    def __init__(self, coordenadas, parede):
        self.coordenadas = coordenadas
        self.parede = parede
        self.vizinhos = []

# arquivo_mapa = open("dia_22_exemplo.txt", "r")
arquivo_mapa = open("dia_22_input.txt", "r")
linhas_mapa = arquivo_mapa.read().split("\n")
arquivo_mapa.close()
direcoes = tuple([(1, 0), (0, 1), (-1, 0), (0, -1)])

largura = 0
for y in range(len(linhas_mapa) - 2):
    largura = max(largura, len(linhas_mapa[y]))
altura = len(linhas_mapa) - 2

mapa = {}
for y in range(altura):
    for x in range(len(linhas_mapa[y])):
        if linhas_mapa[y][x] != " ":
            mapa[tuple([x, y])] = (Posicao(tuple([x, y]), linhas_mapa[y][x] == "#"))

for posicao in mapa:
    for direcao in direcoes:
        x = (posicao[0] + direcao[0]) % largura
        y = (posicao[1] + direcao[1]) % altura

        while tuple([x, y]) not in mapa:
            x = (x + direcao[0]) % largura
            y = (y + direcao[1]) % altura
        
        mapa[posicao].vizinhos.append(mapa[tuple([x, y])])

posicao_atual = None
for x in range(largura):
    if tuple([x, 0]) in mapa:
        posicao_atual = mapa[tuple([x, 0])]

caminho = []
instrucao = ""
for char in linhas_mapa[-1]:
    if char.isnumeric():
        instrucao += char
    else:
        caminho.append(int(instrucao))
        instrucao = ""
        caminho.append(char)
caminho.append(int(instrucao))

direcao = 0
for instrucao in caminho:
    if not type(instrucao) is int:
        direcao += 1 if instrucao == "R" else (-1)
        direcao = direcao % 4
    else:
        distancia = instrucao
        while distancia > 0 and not posicao_atual.vizinhos[direcao].parede:
            distancia -= 1
            posicao_atual = posicao_atual.vizinhos[direcao]

senha = ((posicao_atual.coordenadas[1] + 1) * 1000) + ((posicao_atual.coordenadas[0] + 1) * 4) + direcao
print(f"Senha = {senha}")