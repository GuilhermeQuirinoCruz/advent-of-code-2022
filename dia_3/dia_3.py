# arquivo_mochilas = open("dia_3_exemplo.txt", "r")
arquivo_mochilas = open("dia_3_input.txt", "r")
dados_mochilas = arquivo_mochilas.read()
lista_mochilas = dados_mochilas.split("\n")
arquivo_mochilas.close()

# retorna o valor unicode do caractere, ajustado pro intervalo correspondente
def prioridade_item(item):
    prioridade = ord(item)

    return (prioridade - 96) if prioridade >= 97 else (prioridade - 38)

def soma_prioridade_itens(itens):
    soma_prioridades = 0
    for item in itens:
        soma_prioridades += prioridade_item(item)
    
    return soma_prioridades

# PARTE 1
lista_itens_repetidos = []

# passa por cada mochila, divide os itens em dois compartimentos e encontra o item repetido
for mochila in lista_mochilas:
    meio = int(len(mochila) / 2)
    compartimento_1 = mochila[0:meio]
    compartimento_2 = mochila[meio:len(mochila)]

    for item in compartimento_1:
        if item in compartimento_2:
            lista_itens_repetidos.append(item)
            break

print(soma_prioridade_itens(lista_itens_repetidos))

# PARTE 2
lista_itens_repetidos.clear()

# passa por cada trio de mochilas e encontra o item que repete em todas
for i in range(0, len(lista_mochilas), 3):
    mochila_1 = lista_mochilas[i]
    mochila_2 = lista_mochilas[i + 1]
    mochila_3 = lista_mochilas[i + 2]

    for item in mochila_1:
        if item in mochila_2 and item in mochila_3:
            lista_itens_repetidos.append(item)
            break

print(soma_prioridade_itens(lista_itens_repetidos))