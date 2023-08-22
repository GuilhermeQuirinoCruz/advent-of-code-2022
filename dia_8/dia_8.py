class Arvore:
    def __init__(self, altura):
        self.altura = altura
        self.visivel = False
        self.pontuacao_cenica = 1

# arquivo_alturas = open("dia_8_exemplo.txt", "r")
arquivo_alturas = open("dia_8_input.txt", "r")
dados_alturas = arquivo_alturas.read()
arquivo_alturas.close()

matriz_arvores = []

for linha in dados_alturas.split("\n"):
    alturas = []
    for altura in linha:
        nova_arvore = Arvore(int(altura))
        alturas.append(nova_arvore)

    matriz_arvores.append(alturas)

def definir_visibilidade_arvores(arvores, direcao):
    maior_altura = -1
    for arvore in arvores[::direcao]:
        if arvore.altura > maior_altura:
            arvore.visivel = True
            maior_altura = arvore.altura
        if arvore.altura == 9:
            break

def definir_visibilidade_horizontal():
    for linha in matriz_arvores:
        definir_visibilidade_arvores(linha, 1)
        definir_visibilidade_arvores(linha, -1)

def formar_coluna_arvores(indice_coluna):
    coluna_arvores = []
    for linha_arvores in matriz_arvores:
        coluna_arvores.append(linha_arvores[indice_coluna])
    
    return coluna_arvores

def definir_visibilidade_vertical():
    qtd_colunas = len(matriz_arvores[0])
    for coluna in range(qtd_colunas):
        coluna_arvores = formar_coluna_arvores(coluna)
        
        definir_visibilidade_arvores(coluna_arvores, 1)
        definir_visibilidade_arvores(coluna_arvores, -1)

definir_visibilidade_horizontal()
definir_visibilidade_vertical()

# PARTE 1
arvores_visiveis = 0

for linha in matriz_arvores:
    for arvore in linha:
        if arvore.visivel:
            arvores_visiveis += 1

print("Quantidade de árvores visíveis:")
print(arvores_visiveis)

# PARTE 2
def calcular_pontuacao_cenica(arvores, posicao, direcao):
    arvore_calcular = arvores[posicao]
    qtd_arvores_visiveis = 0
    for arvore in arvores[posicao::direcao]:
        if arvore == arvore_calcular:
            continue
        
        qtd_arvores_visiveis += 1
        if arvore.altura >= arvore_calcular.altura:
            break
    
    arvore_calcular.pontuacao_cenica *= qtd_arvores_visiveis

qtd_colunas = len(matriz_arvores[0])

for linha in matriz_arvores:
    for posicao in range(qtd_colunas):
        if linha[posicao].pontuacao_cenica != 0:
            calcular_pontuacao_cenica(linha, posicao, 1)
            calcular_pontuacao_cenica(linha, posicao, -1)

for coluna in range(qtd_colunas):
    coluna_arvores = formar_coluna_arvores(coluna)
    for posicao in range(qtd_colunas):
        if coluna_arvores[posicao].pontuacao_cenica != 0:
            calcular_pontuacao_cenica(coluna_arvores, posicao, 1)
            calcular_pontuacao_cenica(coluna_arvores, posicao, -1)

def imprimir_pontuacoes_cenicas():
    for linha in matriz_arvores:
        linha_pontuacao = []
        for arvore in linha:
            linha_pontuacao.append(arvore.pontuacao_cenica)
        
        print(linha_pontuacao)

maior_pontuacao_cenica = 0
for linha in matriz_arvores:
    for arvore in linha:
        if arvore.pontuacao_cenica > maior_pontuacao_cenica:
            maior_pontuacao_cenica = arvore.pontuacao_cenica

print("Maior pontuação cênica:")
print(maior_pontuacao_cenica)