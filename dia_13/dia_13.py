# arquivo_pacotes = open("dia_13_exemplo.txt", "r")
arquivo_pacotes = open("dia_13_input.txt", "r")
dados_pacotes = arquivo_pacotes.read()
pares_pacotes = dados_pacotes.split("\n")
arquivo_pacotes.close()

def adicionar_itens(itens, lista, inicio, fim):
    for item in lista[inicio:fim].split(","):
        item = item.strip("[]")
        if item != "":
            itens.append(int(item))

def criar_itens_pacote(lista, inicio):
    meus_itens = []
    inicio += 1
    indice = inicio
    while indice < len(lista):
        if lista[indice] == "[":
            adicionar_itens(meus_itens, lista, inicio, indice)

            itens_adicionar, indice = criar_itens_pacote(lista, indice)
            meus_itens.append(itens_adicionar)
            inicio = indice + 1
        elif lista[indice] == "]":
            adicionar_itens(meus_itens, lista, inicio, indice)
            break
        
        indice += 1
    
    return meus_itens, indice

def comparar_pacotes(esquerdo, direito):
    continuar = True
    ordenado = True

    if len(esquerdo) == 0 and len(direito) > 0:
        continuar = False

    for i in range(max(len(esquerdo), len(direito))):
        if not continuar:
            break

        # lado direito acabou
        if i >= len(direito):
            continuar = False
            ordenado = False
            break
        
        # lado esquerdo acabou
        if i >= len(esquerdo):
            continuar = False
            ordenado = True
            break

        valor_esquerda = esquerdo[i]
        valor_direita = direito[i]

        if type(valor_esquerda) == int and type(valor_direita) == int:
            if valor_esquerda < valor_direita:
                continuar = False
            else:
                continuar = valor_esquerda == valor_direita
                ordenado = continuar
        else:
            if type(valor_esquerda) != list:
                valor_esquerda = [valor_esquerda]
            if type(valor_direita) != list:
                valor_direita = [valor_direita]
            
            continuar, ordenado = comparar_pacotes(valor_esquerda, valor_direita)

    return continuar, ordenado

# PARTE 1
soma_indices_pares_ordenados = 0
pacotes = []
for indice_par in range(0, len(pares_pacotes), 3):
    esquerdo = criar_itens_pacote(pares_pacotes[indice_par], 0)[0]
    direito = criar_itens_pacote(pares_pacotes[indice_par + 1], 0)[0]

    pacotes.append(esquerdo)
    pacotes.append(direito)

    if comparar_pacotes(esquerdo, direito)[1]:
        indice = int(indice_par / 3) + 1
        soma_indices_pares_ordenados += indice

print(soma_indices_pares_ordenados)

# PARTE 2
pacotes_divisores = [[[2]], [[6]]]
pacotes.extend(pacotes_divisores)

# bubble sort de lei
ordenado = False
while not ordenado:
    ordenado = True
    for i in range(len(pacotes) - 1):
        if not comparar_pacotes(pacotes[i], pacotes[i + 1])[1]:
            pacotes[i], pacotes[i + 1] = pacotes[i + 1], pacotes[i]
            ordenado = False

indices_pacotes_divisores = []
for indice_pacote in range(len(pacotes)):
    print(f"{indice_pacote} : {pacotes[indice_pacote]}")
    if pacotes[indice_pacote] in pacotes_divisores:
        indices_pacotes_divisores.append(indice_pacote + 1)

print(indices_pacotes_divisores[0] * indices_pacotes_divisores[1])