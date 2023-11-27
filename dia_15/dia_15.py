class Sensor:
    def __init__(self, posicao, sinalizador):
        self.posicao = posicao
        self.distancia_sinalizador = abs(sinalizador[0] - posicao[0]) + abs(sinalizador[1] - posicao[1])

# arquivo_sensores = open("dia_15_exemplo.txt", "r")
arquivo_sensores = open("dia_15_input.txt", "r")
dados_sensores = arquivo_sensores.read()
arquivo_sensores.close()

def posicao_dado(posicao):
    posicao = posicao.split(",")
    coordenadas = []
    for coordenada in posicao:
        coordenada = coordenada.split("=")
        coordenadas.append(int(coordenada[-1]))
    
    return coordenadas

sensores = []
sinalizadores = []
x_sinalizadores_linha_2_milhoes = set()

for dado in dados_sensores.split("\n"):
    dado = dado.split(":")

    posicao_sensor = posicao_dado(dado[0])
    posicao_sinalizador = posicao_dado(dado[1])

    novo_sensor = Sensor(posicao_sensor, posicao_sinalizador)
    sensores.append(novo_sensor)

    sinalizadores.append(posicao_sinalizador)
    if posicao_sinalizador[1] == 2000000:
        x_sinalizadores_linha_2_milhoes.add(posicao_sinalizador[0])

# Solução inviável
# ---------------------------------------------------------------------------------------
posicoes_sem_sinalizador = {}

def incluir_posicao_sem_sinalizador(posicao):
    if posicao in sinalizadores:
        return
    
    if posicao[1] not in posicoes_sem_sinalizador:
        posicoes_sem_sinalizador[posicao[1]] = {posicao[0]}
    else:
        posicoes_sem_sinalizador[posicao[1]].add(posicao[0])

def incluir_posicoes_sem_sinalizador(sensor):
    qtd = 1
    add_y = sensor.distancia_sinalizador
    while add_y >= 0:
        x = sensor.posicao[0] - (qtd // 2)
        for i in range(qtd):
            incluir_posicao_sem_sinalizador([x + i, sensor.posicao[1] - add_y])
            if add_y != 0:
                incluir_posicao_sem_sinalizador([x + i, sensor.posicao[1] + add_y])
        
        qtd += 2
        add_y -= 1
# ---------------------------------------------------------------------------------------

# PARTE 1
linha_2_milhoes = set()

def adicionar_posicoes_linha_2_milhoes(sensor):
    if sensor.posicao[1] + sensor.distancia_sinalizador < 2000000 or \
        sensor.posicao[1] - sensor.distancia_sinalizador > 2000000:
        return
    
    distancia_linha = abs(sensor.posicao[1] - 2000000)
    qtd_linha = 1 + (2 * abs(sensor.distancia_sinalizador - distancia_linha))

    x = sensor.posicao[0] - (qtd_linha // 2)
    for i in range(qtd_linha):
        linha_2_milhoes.add(x + i)

# for sensor in sensores:
#     adicionar_posicoes_linha_2_milhoes(sensor)

# print(len(linha_2_milhoes) - len(x_sinalizadores_linha_2_milhoes))

# PARTE 1 APRIMORADA
limites_x = [sensores[0].posicao[0], sensores[0].posicao[0]]

def calcular_limites_linha_2_milhoes(sensor):
    if sensor.posicao[1] + sensor.distancia_sinalizador < 2000000 or \
        sensor.posicao[1] - sensor.distancia_sinalizador > 2000000:
        return

    distancia_linha = abs(sensor.posicao[1] - 2000000)
    qtd_linha = 1 + (2 * abs(sensor.distancia_sinalizador - distancia_linha))

    x_inicio = sensor.posicao[0] - (qtd_linha // 2)
    x_fim = x_inicio + (qtd_linha - 1)

    limites_x[0] = min(limites_x[0], x_inicio)
    limites_x[1] = max(limites_x[1], x_fim)

for sensor in sensores:
    calcular_limites_linha_2_milhoes(sensor)

print((limites_x[1] - limites_x[0] + 1) - len(x_sinalizadores_linha_2_milhoes))

# PARTE 2
sensores.sort(key = lambda s:s.distancia_sinalizador, reverse=True)

def posicao_dentro_do_alcance(posicao, sensor):
    distancia = abs(posicao[0] - sensor.posicao[0]) + abs(posicao[1] - sensor.posicao[1])
    
    return distancia <= sensor.distancia_sinalizador

def proximo_x_verificar(posicao, sensor):
    distancia_vertical = abs(sensor.posicao[1] - posicao[1])
    qtd_linha = 1 + (2 * abs(sensor.distancia_sinalizador - distancia_vertical))
    
    return sensor.posicao[0] + (qtd_linha // 2) + 1

posicao_sinalizador_alvo = [0, 0]
posicao_encontrada = False
while posicao_sinalizador_alvo[1] <= 4000000 and not posicao_encontrada:
    while posicao_sinalizador_alvo[0] <= 4000000 and not posicao_encontrada:
        posicao_encontrada = True
        for sensor in sensores:
            if posicao_dentro_do_alcance(posicao_sinalizador_alvo, sensor):
                posicao_sinalizador_alvo[0] = proximo_x_verificar(posicao_sinalizador_alvo, sensor)
                posicao_encontrada = False
                break
    
    if not posicao_encontrada:
        posicao_sinalizador_alvo[0] = 0
        posicao_sinalizador_alvo[1] += 1

print(posicao_sinalizador_alvo)

frequencia_ajuste = (posicao_sinalizador_alvo[0] * 4000000) + posicao_sinalizador_alvo[1]
print(frequencia_ajuste)