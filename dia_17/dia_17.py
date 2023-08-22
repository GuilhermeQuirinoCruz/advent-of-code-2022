class Pedra:
    def __init__(self, tipo):
        self.posicoes = []
        match(tipo):
            case 0:
                self.posicoes = [[0, 0], [1, 0], [2, 0], [3, 0]]
            case 1:
                self.posicoes = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
            case 2:
                self.posicoes = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]]
            case 3:
                self.posicoes = [[0, 0], [0, 1], [0, 2], [0, 3]]
            case 4:
                self.posicoes = [[0, 0], [1, 0], [0, 1], [1, 1]]

# arquivo_jatos = open("dia_17_exemplo.txt", "r")
arquivo_jatos = open("dia_17_input.txt", "r")
dados_jatos = arquivo_jatos.read()
direcao_jatos = list(dados_jatos)
arquivo_jatos.close()

def posicao_inicial_pedra(pedra, x, y):
    for posicao in pedra.posicoes:
        posicao[0] += x
        posicao[1] += y
    
def posicao_valida(posicao, posicoes_ocupadas):
    x_valido = posicao[0] >= 0 and posicao[0] <= 6
    y_valido = posicao[1] >= 0
    posicao_ocupada = posicao[1] in posicoes_ocupadas and posicao[0] in posicoes_ocupadas[posicao[1]]

    return (x_valido and y_valido) and not posicao_ocupada

def mover_pedra(pedra, direcao, posicoes_ocupadas):
    proximas_posicoes = list(pedra.posicoes)
    for i in range(len(proximas_posicoes)):
        posicao_movimento = [proximas_posicoes[i][0] + direcao[0], proximas_posicoes[i][1] + direcao[1]]
        if posicao_valida(posicao_movimento, posicoes_ocupadas):
            proximas_posicoes[i] = posicao_movimento
            continue
        return False
    
    pedra.posicoes = list(proximas_posicoes)
    return True

def ocupar_posicoes(pedra, posicoes_ocupadas):
    for posicao in pedra.posicoes:
        if posicao[1] not in posicoes_ocupadas:
            posicoes_ocupadas[posicao[1]] = [posicao[0]]
        else:
            posicoes_ocupadas[posicao[1]].append(posicao[0])

def altura_pedra(pedra):
    return pedra.posicoes[-1][1] + 1

def simular_pedras(pedras_restantes, tipo_pedra, indice_jato, interromper):
    posicoes_ocupadas = {}
    altura_torre = 0
    pedra_atual = Pedra(tipo_pedra)
    pedras_colocadas = 0
    posicao_inicial_pedra(pedra_atual, 2, 3)
    while pedras_restantes > 0:
        pedras_restantes -= 1
        pedras_colocadas += 1
        while True:
            jato_atual = direcao_jatos[indice_jato]
            mover_pedra(pedra_atual, [-1, 0] if jato_atual == "<" else [1, 0], posicoes_ocupadas)
            indice_jato = (indice_jato + 1) % len(direcao_jatos)
            if not mover_pedra(pedra_atual, [0, -1], posicoes_ocupadas):
                ocupar_posicoes(pedra_atual, posicoes_ocupadas)
                break
        
        altura_torre = max(altura_torre, altura_pedra(pedra_atual))
        tipo_pedra = (tipo_pedra + 1) % 5
        pedra_atual = Pedra(tipo_pedra)
        posicao_inicial_pedra(pedra_atual, 2, altura_torre + 3)

        if interromper and len(posicoes_ocupadas[altura_torre - 1]) == 7:
            break

    return [pedras_colocadas, tipo_pedra, indice_jato, altura_torre]

# PARTE 1
# qtd_pedras = 2022
# PARTE 2
qtd_pedras = 1000000000000

# print(simular_pedras(10000, 0, 0, False)) = 15537
# print(simular_pedras(5000, 0, 0, False)) = 7714
# print(simular_pedras(100000, 0, 0, False)) = 156180

altura_torre = 0
indice_direcao_jato = 0
tipo_pedra_atual = 0
simulacoes_anteriores = {}

while qtd_pedras > 0:
    simulacao = None
    chave_simulacao = tuple([tipo_pedra_atual, indice_direcao_jato])
    if chave_simulacao in simulacoes_anteriores:
        soma_pedras = 0
        soma_alturas = 0
        for par_chave in simulacoes_anteriores:
            if par_chave != tuple([0, 0]):
                soma_pedras += simulacoes_anteriores[par_chave][0]
                soma_alturas += simulacoes_anteriores[par_chave][3]
        
        repeticoes = qtd_pedras // soma_pedras
        altura_torre += soma_alturas * repeticoes
        qtd_pedras = qtd_pedras % soma_pedras

        simulacao = simular_pedras(qtd_pedras, tipo_pedra_atual, indice_direcao_jato, False)
    else:
        simulacao = simular_pedras(qtd_pedras, tipo_pedra_atual, indice_direcao_jato, True)
        simulacoes_anteriores[chave_simulacao] = simulacao

    qtd_pedras -= simulacao[0]
    tipo_pedra_atual = simulacao[1]
    indice_direcao_jato = simulacao[2]
    altura_torre += simulacao[3]

    print(qtd_pedras)

print(simulacoes_anteriores)
print(f"Altura da torre de pedras: {altura_torre}")