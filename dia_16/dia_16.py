class Valvula:
    def __init__(self, nome, vazao, vizinhas):
        self.nome = nome
        self.taxa_vazao = vazao
        self.valvulas_vizinhas = vizinhas
        self.distancias = {}

# class Simulacao:
#     def __init__(self, valvula_atual, valvulas_visitadas, minutos_restantes, pressao_liberada, caminho):
#         self.valvula_atual = valvula_atual
#         self.valvulas_visitadas = valvulas_visitadas
#         self.minutos_restantes = minutos_restantes
#         self.pressao_liberada = pressao_liberada

#         self.caminho = caminho

class Simulacao:
    def __init__(self, valvulas_visitadas, minutos_restantes, pressao_liberada, parceiros, caminho):
        self.valvulas_visitadas = valvulas_visitadas
        self.minutos_restantes = minutos_restantes
        self.pressao_liberada = pressao_liberada
        self.parceiros = parceiros

        self.caminho = caminho

class Parceiro:
    def __init__(self, valvula, minuto, nome, abrir):
        self.valvula_atual = valvula
        self.minuto_chegada = minuto
        self.abrir_valvula = abrir
        
        self.nome = nome

# arquivo_valvulas = open("dia_16_exemplo.txt", "r")
arquivo_valvulas = open("dia_16_input.txt", "r")
dados_valvulas = arquivo_valvulas.read()
arquivo_valvulas.close()

valvulas = []
valvula_inicial = None

for valvula in dados_valvulas.split("\n"):
    valvula, tuneis = valvula.split(";")

    valvula = valvula.split(" ")
    nome = valvula[1]
    vazao = int(valvula[-1].split("=")[1])

    tuneis = tuneis.split("valve")[1].strip("s").strip(" ")
    tuneis = tuneis.replace(" ", "").split(",")
    
    nova_valvula = Valvula(nome, vazao, tuneis)
    valvulas.append(nova_valvula)

    if nome == "AA":
        valvula_inicial = nova_valvula

for valvula in valvulas:
    vizinhas = []
    for possivel_vizinha in valvulas:
        if possivel_vizinha.nome in valvula.valvulas_vizinhas:
            vizinhas.append(possivel_vizinha)
    
    valvula.valvulas_vizinhas = vizinhas

# PARTE 1 que quase deu certo
def menor_caminho(valvula_inicial, valvula_final):
    caminhos = [[valvula_inicial]]
    indice_caminho = 0
    valvulas_visitadas = set()

    while indice_caminho < len(caminhos):
        caminho_atual = caminhos[indice_caminho]
        ultima_valvula = caminho_atual[-1]

        proximas_valvulas = ultima_valvula.valvulas_vizinhas
        if valvula_final in proximas_valvulas:
            caminho_atual.append(valvula_final)
            return caminho_atual
        
        for valvula in proximas_valvulas:
            if not valvula in valvulas_visitadas:
                novo_caminho = caminho_atual[:]
                novo_caminho.append(valvula)
                caminhos.append(novo_caminho)

                valvulas_visitadas.add(valvula)
        
        indice_caminho += 1
    
    return []

for valvula in valvulas:
    for valvula_destino in valvulas:
        if valvula != valvula_destino and (valvula_destino.taxa_vazao != 0 or valvula_destino == valvula_inicial):
            valvula.distancias[valvula_destino] = len(menor_caminho(valvula, valvula_destino)) - 1

valvulas_nao_zeradas = []
for valvula in valvulas:
    if valvula.taxa_vazao != 0 or valvula == valvula_inicial:
        valvulas_nao_zeradas.append(valvula)

valvulas = list(valvulas_nao_zeradas)

# def potencial_valvula(valvula_atual, valvula_alvo, minutos_restantes):
#     minutos_pos_movimento = minutos_restantes - valvula_atual.distancias[valvula_alvo] - 1
#     return (valvula_alvo.taxa_vazao * minutos_pos_movimento) / valvula_atual.distancias[valvula_alvo]

# def distancia_media_outras_valvulas(valvula_alvo, valvulas):
#     soma_distancias = 0
#     valvulas_consideradas = 0
#     for valvula in valvula_alvo.distancias:
#         if valvula in valvulas:
#             soma_distancias += valvula_alvo.distancias[valvula]
#             valvulas_consideradas += 1
    
#     return soma_distancias / max(valvulas_consideradas, 1)

# minutos_restantes = 30
# pressao_liberada = 0
# valvula_atual = valvula_inicial

# caminho = "AA"
# while minutos_restantes > 0:
#     valvula_maior_potencial = None
#     maior_potencial = -1000
#     for valvula in valvulas:
#         if valvula != valvula_atual:
#             potencial = potencial_valvula(valvula_atual, valvula, minutos_restantes)
#             potencial /= distancia_media_outras_valvulas(valvula, valvulas)
#             if potencial > maior_potencial:
#                 maior_potencial = potencial
#                 valvula_maior_potencial = valvula
    
#     if valvula_maior_potencial == None:
#         minutos_restantes = 0
#         break

#     minutos_restantes -= (1 + valvula_atual.distancias[valvula_maior_potencial])
#     if maior_potencial > 0:
#         pressao_liberada += (valvula_maior_potencial.taxa_vazao * minutos_restantes)
#         valvulas.remove(valvula_atual)
#         valvula_atual = valvula_maior_potencial
#         caminho += "->" + valvula_atual.nome

# print(pressao_liberada)
# print(caminho)

# PARTE 1 agora vai
# simulacoes = [Simulacao(valvula_inicial, [], 30, 0, "")]
# maior_pressao_liberada = 0
# while len(simulacoes) > 0:
#     simulacao = simulacoes.pop()
#     while simulacao.minutos_restantes > 0:
#         simulacao.caminho += "->" + simulacao.valvula_atual.nome
#         simulacao.pressao_liberada += simulacao.minutos_restantes * simulacao.valvula_atual.taxa_vazao
#         simulacao.valvulas_visitadas.append(simulacao.valvula_atual)

#         proximas_simulacoes = []
#         for valvula in valvulas:
#             if valvula == simulacao.valvula_atual or valvula in simulacao.valvulas_visitadas:
#                 continue
            
#             distancia = simulacao.valvula_atual.distancias[valvula]
#             if distancia < simulacao.minutos_restantes:
#                 nova_simulacao = Simulacao(valvula, list(simulacao.valvulas_visitadas),
#                     simulacao.minutos_restantes - distancia - 1, simulacao.pressao_liberada, simulacao.caminho)
#                 proximas_simulacoes.append(nova_simulacao)

#         if len(proximas_simulacoes) == 0:
#             break
        
#         proxima = proximas_simulacoes.pop()
#         simulacao = proxima

#         simulacoes.extend(proximas_simulacoes)
    
#     # print(simulacao.caminho)
#     # print(simulacao.pressao_liberada)
#     maior_pressao_liberada = max(maior_pressao_liberada, simulacao.pressao_liberada)

# print(maior_pressao_liberada)

def copiar_parceiro(parceiro):
    return Parceiro(parceiro.valvula_atual, parceiro.minuto_chegada, parceiro.nome, parceiro.abrir_valvula)

eu = Parceiro(valvula_inicial, 26, "eu", False)
elefante = Parceiro(valvula_inicial, 26, "elefante", False)
simulacoes = [Simulacao([valvula_inicial], 26, 0, [eu, elefante], "")]

maior_pressao_liberada = 0
# limite_simulacoes = 5000000
qtd_simulacoes = 0
# caminhos = set()
while len(simulacoes) > 0:
    # limite_simulacoes -= 1
    qtd_simulacoes += 1
    simulacao = simulacoes.pop()
    while simulacao.minutos_restantes > 0:
        # print(f"({simulacao.caminho}) Minuto: {simulacao.minutos_restantes}")
        for parceiro in simulacao.parceiros:
            if simulacao.minutos_restantes > parceiro.minuto_chegada:
                # print(f"{parceiro.nome} ainda não chegou em {parceiro.valvula_atual.nome}({parceiro.minuto_chegada})")
                continue

            if parceiro.abrir_valvula:
                simulacao.caminho += "->" + parceiro.nome + ":"
                simulacao.caminho += parceiro.valvula_atual.nome + f"({simulacao.minutos_restantes})"
                simulacao.pressao_liberada += simulacao.minutos_restantes * parceiro.valvula_atual.taxa_vazao

                parceiro.abrir_valvula = False

            proximas_simulacoes = []
            valvula_anterior = parceiro.valvula_atual
            for valvula in valvulas:
                if valvula in simulacao.valvulas_visitadas or valvula == valvula_anterior:
                    continue
                
                distancia = valvula_anterior.distancias[valvula]
                if distancia < simulacao.minutos_restantes:
                    parceiro.abrir_valvula = True
                    parceiro.valvula_atual = valvula
                    parceiro.minuto_chegada = simulacao.minutos_restantes - distancia - 1

                    copia_parceiros = []
                    for copia in simulacao.parceiros:
                        copia_parceiros.append(copiar_parceiro(copia))

                    nova_simulacao = Simulacao(
                        simulacao.valvulas_visitadas.copy(),
                        simulacao.minutos_restantes,
                        simulacao.pressao_liberada,
                        copia_parceiros,
                        simulacao.caminho)
                    nova_simulacao.valvulas_visitadas.append(valvula)
                    proximas_simulacoes.append(nova_simulacao)

            if len(proximas_simulacoes) == 0:
                continue
            
            proximas_simulacoes.pop()
            simulacao.valvulas_visitadas.append(parceiro.valvula_atual)

            simulacoes.extend(proximas_simulacoes)
        
        simulacao.minutos_restantes -= 1
    
    maior_pressao_liberada = max(maior_pressao_liberada, simulacao.pressao_liberada)
    # for valvula in simulacao.valvulas_visitadas:
    #     print(valvula.nome)
    # print(simulacao.pressao_liberada)
    # print(simulacao.caminho)
    # caminhos.add(simulacao.caminho)
    # print("---")

# print(limite_simulacoes)
# print(len(caminhos))
print(f"Qtd: {qtd_simulacoes}")
print(maior_pressao_liberada)

# 1000000: 2215 baixo
# 5000000: 2551 baixo
# 66531283: 2723