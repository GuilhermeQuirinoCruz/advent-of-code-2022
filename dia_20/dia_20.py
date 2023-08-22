class Numero:
    def __init__(self, valor, anterior, proximo):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

# arquivo_numeros = open("dia_20_exemplo.txt", "r")
arquivo_numeros = open("dia_20_input.txt", "r")
dados_numeros = arquivo_numeros.read()
arquivo_numeros.close()

numeros = []
qtd_numeros = 0
primeiro_numero = None
numero_zero = None
anterior = None

for valor in dados_numeros.split("\n"):
    valor = int(valor)
    novo_numero = Numero(valor, anterior, None)

    if not primeiro_numero:
        primeiro_numero = novo_numero

    if anterior:
        anterior.proximo = novo_numero
    anterior = novo_numero
    
    if valor == 0:
        numero_zero = novo_numero
    
    numeros.append(novo_numero)
    qtd_numeros += 1

primeiro_numero.anterior = numeros[-1]
numeros[-1].proximo = primeiro_numero

def imprimir_numeros():
    inicio = numeros[0]
    atual = inicio.proximo
    saida = f"{inicio.valor}"
    while atual != inicio:
        saida += f" > {atual.valor}"
        atual = atual.proximo
    
    print(saida)

def avancar_numero(inicio, passos, frente):
    numero = inicio
    while passos > 0:
        passos -= 1
        numero = numero.proximo if frente else numero.anterior
    
    return numero

def destino_numero(numero):
    passos = (abs(numero.valor) % qtd_numeros) + (1 if numero.valor < 0 else 0)
    # passos = abs(numero.valor) + (1 if numero.valor < 0 else 0)
    
    destino = numero.anterior if passos == 0 else avancar_numero(numero, passos, numero.valor > 0)
    
    return destino

def mixar_numeros():
    global qtd_numeros
    for numero_atual in numeros:
        if numero_atual.valor == 0:
            continue

        numero_atual.anterior.proximo = numero_atual.proximo
        numero_atual.proximo.anterior = numero_atual.anterior

        qtd_numeros -= 1
        destino = destino_numero(numero_atual)
        qtd_numeros += 1

        numero_atual.proximo = destino.proximo
        numero_atual.proximo.anterior = numero_atual

        destino.proximo = numero_atual
        numero_atual.anterior = destino

        # imprimir_numeros()

# PARTE 1
# mixar_numeros()

# PARTE 2
chave_decriptacao = 811589153
for numero in numeros:
    numero.valor *= chave_decriptacao

vezes = 10
while vezes > 0:
    vezes -= 1
    mixar_numeros()

coordenadas = []
for i in range(3):
    passos = (1000 + (1000 * i)) % qtd_numeros
    numero = avancar_numero(numero_zero, passos, True)
    coordenadas.append(numero.valor)

# imprimir_numeros()

print(f"Coordenadas: {coordenadas}")
print(f"Soma das coordenadas: {sum(coordenadas)}")