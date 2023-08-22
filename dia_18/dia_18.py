# arquivo_lava = open("dia_18_exemplo.txt", "r")
arquivo_lava = open("dia_18_input.txt", "r")
dados_lava = arquivo_lava.read()
gotas_lava = dados_lava.split("\n")
arquivo_lava.close()

cubos_lava = set()
limites_x = [100, 0]
limites_y = [100, 0]
limites_z = [100, 0]

for gota in gotas_lava:
    gota = gota.split(",")
    coordenadas = []
    for coordenada in gota:
        coordenadas.append(int(coordenada))

    cubos_lava.add(tuple(coordenadas))

    limites_x = [min(limites_x[0], coordenadas[0] - 1), max(limites_x[1], coordenadas[0] + 1)]
    limites_y = [min(limites_y[0], coordenadas[1] - 1), max(limites_y[1], coordenadas[1] + 1)]
    limites_z = [min(limites_z[0], coordenadas[2] - 1), max(limites_z[1], coordenadas[2] + 1)]

cubo_expandido = []
for x in range(limites_x[0], limites_x[1] + 1):
    for y in range(limites_y[0], limites_y[1] + 1):
        for z in range(limites_z[0], limites_z[1] + 1):
            cubo_expandido.append(tuple([x, y, z]))

def cubos_adjacentes(cubo):
    add_x = [1, -1, 0, 0, 0, 0]
    add_y = [0, 0, 1, -1, 0, 0]
    add_z = [0, 0, 0, 0, 1, -1]
    adjacentes = []
    for i in range(6):
        x = cubo[0] + add_x[i]
        y = cubo[1] + add_y[i]
        z = cubo[2] + add_z[i]
        adjacentes.append(tuple([x, y, z]))
    
    return adjacentes

def qtd_cubos_adjacentes(cubo, grupo):
    qtd = 0
    adjacentes = cubos_adjacentes(cubo)
    for cubo in adjacentes:
        qtd += 1 if cubo in grupo else 0

    return qtd

def calcular_area_superficie(cubos):
    area = 0
    for cubo in cubos:
        area += 6 - qtd_cubos_adjacentes(cubo, cubos)
    
    return area

# PARTE 1
area_superficie = calcular_area_superficie(cubos_lava)
print(f"Área de superfície total: {area_superficie}")

# PARTE 2
def posicao_valida(coordenada):
    x_valido = coordenada[0] >= limites_x[0] and coordenada[0] <= limites_x[1]
    y_valido = coordenada[1] >= limites_y[0] and coordenada[1] <= limites_y[1]
    z_valido = coordenada[2] >= limites_z[0] and coordenada[2] <= limites_z[1]

    return x_valido and y_valido and z_valido and coordenada not in cubos_lava

def cubos_adjacentes_validos(cubo):
    adjacentes_validos = []
    for cubo_verificar in cubos_adjacentes(cubo):
        if posicao_valida(cubo_verificar):
            adjacentes_validos.append(cubo_verificar)
    
    return adjacentes_validos

def remover_cubos(cubo_origem, cubos_remover):
    for cubo in cubos_remover:
        if cubo in cubo_origem:
            cubo_origem.remove(cubo)

    return cubo_origem

def preencher_espacos(cubo_origem):
    espacos_preenchidos = set()
    espacos_preenchidos.add(cubo_origem[0])
    cubos_verificar = cubos_adjacentes_validos(cubo_origem[0])
    
    while len(cubos_verificar) > 0:
        cubo = cubos_verificar.pop()
        cubos_adjacentes = cubos_adjacentes_validos(cubo)
        for cubo_preencher in cubos_adjacentes:
            if not cubo_preencher in espacos_preenchidos:
                espacos_preenchidos.add(cubo_preencher)
                cubos_verificar.append(cubo_preencher)
    
    cubo_origem = remover_cubos(cubo_origem, espacos_preenchidos)
    cubo_origem = remover_cubos(cubo_origem, cubos_lava)

    return calcular_area_superficie(cubo_origem)

area_superficie -= preencher_espacos(cubo_expandido)
print(f"Área de superfície exterior: {area_superficie}")