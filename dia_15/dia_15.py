class Sensor:
    def __init__(self, posicao, sinalizador):
        self.posicao = posicao
        self.sinalizador_mais_proximo = sinalizador

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
x_sinalizadores_linha_2kk = set()

for dado in dados_sensores.split("\n"):
    dado = dado.split(":")

    posicao_sensor = posicao_dado(dado[0])
    posicao_sinalizador = posicao_dado(dado[1])

    novo_sensor = Sensor(posicao_sensor, posicao_sinalizador)
    sensores.append(novo_sensor)

    sinalizadores.append(posicao_sinalizador)
    if posicao_sinalizador[1] == 2000000:
        x_sinalizadores_linha_2kk.add(posicao_sinalizador[0])

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

# PARTE 1
linha_2kk = set()

def linha_2_milhoes(sensor):
    if sensor.posicao[1] + sensor.distancia_sinalizador < 2000000 or sensor.posicao[1] - sensor.distancia_sinalizador > 2000000:
        return
    
    distancia_linha = abs(sensor.posicao[1] - 2000000)
    qtd_linha = 1 + (2 * abs(sensor.distancia_sinalizador - distancia_linha))

    x = sensor.posicao[0] - (qtd_linha // 2)
    for i in range(qtd_linha):
        if x + i not in x_sinalizadores_linha_2kk:
            linha_2kk.add(x + i)

# for sensor in sensores:
#     linha_2_milhoes(sensor)
    # incluir_posicoes_sem_sinalizador(sensor)

# print(len(linha_2kk))

# PARTE 2
sensores.sort(key = lambda s:s.distancia_sinalizador, reverse=True)

def posicao_dentro_do_alcance(posicao, sensor):
    distancia = abs(posicao[0] - sensor.posicao[0]) + abs(posicao[1] - sensor.posicao[1])
    return distancia <= sensor.distancia_sinalizador

def proximo_x_verificar(posicao, sensor):
    distancia_vertical = abs(sensor.posicao[1] - posicao[1])
    qtd_linha = 1 + 2 * abs(sensor.distancia_sinalizador - distancia_vertical)
    
    return sensor.posicao[0] + (qtd_linha // 2) + 1

posicao_sinalizador_alvo = [0, 0]
posicao_encontrada = False
while posicao_sinalizador_alvo[1] <= 4000001 and not posicao_encontrada:
    posicao_sinalizador_alvo[0] = 0
    while posicao_sinalizador_alvo[0] <= 4000001 and not posicao_encontrada:
        posicao_encontrada = True
        for sensor in sensores:
            if posicao_dentro_do_alcance(posicao_sinalizador_alvo, sensor):
                posicao_sinalizador_alvo[0] = proximo_x_verificar(posicao_sinalizador_alvo, sensor)
                posicao_encontrada = False
                break
    
    if not posicao_encontrada:
        posicao_sinalizador_alvo[1] += 1

print(posicao_sinalizador_alvo)

frequencia_ajuste = (posicao_sinalizador_alvo[0] * 4000000) + posicao_sinalizador_alvo[1]
print(frequencia_ajuste)