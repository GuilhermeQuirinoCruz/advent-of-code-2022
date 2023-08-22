# arquivo_caixas = open("dia_5_exemplo.txt", "r")
arquivo_caixas = open("dia_5_input.txt", "r")
dados_caixas = arquivo_caixas.read()
lista_caixas = dados_caixas.split("\n")
arquivo_caixas.close()

indice_fim_caixas = lista_caixas.index("") - 1

qtd_pilhas = int(lista_caixas[indice_fim_caixas].split(" ")[-2])
# qtd_pilhas = int(lista_caixas[indice_fim_caixas][-2])

lista_movimentos = lista_caixas[indice_fim_caixas + 2:]
lista_caixas = lista_caixas[:lista_caixas.index("") - 1]

pilhas_caixas = []

for i in range(0, qtd_pilhas):
    nova_pilha = []
    for linha in lista_caixas:
        caixa = linha[4 * i:4 * i + 3]
        if not caixa.isspace():
            caixa = caixa.strip("[]")
            nova_pilha.append(caixa)

    nova_pilha.reverse()
    pilhas_caixas.append(nova_pilha)

def remover_caixas(movimento):
    qtd_caixas = int(movimento[1])
    pilha_remover = int(movimento[3]) - 1

    caixas_mover = []
    for i in range(0, qtd_caixas):
        caixa = pilhas_caixas[pilha_remover].pop()
        caixas_mover.append(caixa)
    
    return caixas_mover

def caixas_no_topo():
    caixas_topo = ""
    for i in range(0, qtd_pilhas):
        if len(pilhas_caixas[i]) > 0:
            caixas_topo += pilhas_caixas[i][-1]
    
    return caixas_topo

# PARTE 1
# for movimento in lista_movimentos:
#     movimento = movimento.split(" ")
#     pilha_chegada = int(movimento[5]) - 1
    
#     pilhas_caixas[pilha_chegada].extend(remover_caixas(movimento))

# print(caixas_no_topo())

# PARTE 2
for movimento in lista_movimentos:
    movimento = movimento.split(" ")
    pilha_chegada = int(movimento[5]) - 1
    
    caixas = remover_caixas(movimento)
    caixas.reverse()
    pilhas_caixas[pilha_chegada].extend(caixas)

print(caixas_no_topo())