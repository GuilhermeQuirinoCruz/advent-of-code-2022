import math

# arquivo_combustivel = open("dia_25_exemplo.txt", "r")
arquivo_combustivel = open("dia_25_input.txt", "r")
dados_combustivel = arquivo_combustivel.read().split("\n")
arquivo_combustivel.close()

valores_base = {0 : [0], 1 : [1], 2 : [2], 3 : [-2, 1], 4 : [-1, 1], 5 : [0, 1], 6 : [1, 1]}

def valor_caractere_decimal(caractere):
    if caractere == "=":
        return -2
    if caractere == "-":
        return -1

    return int(caractere)

def valor_decimal_caractere(decimal):
    if decimal == -2:
        return "="
    if decimal == -1:
        return "-"
    
    return str(decimal)

def converter_requisito_numeros(requisito):
    requisito_convertido = []
    for caractere in requisito:
        requisito_convertido.append(valor_caractere_decimal(caractere))

    return requisito_convertido

# requisitos_combustivel = []
# for requisito in dados_combustivel:
#     requisitos_combustivel.append(converter_requisito_numeros(requisito[::-1]))

def converter_em_decimal(numero):
    decimal = 0
    potencia = 1
    for algarismo in numero[::-1]:
        valor = valor_caractere_decimal(algarismo)
        decimal += valor * potencia
        potencia *= 5
    
    return decimal

requisitos_combustivel = []
for requisito in dados_combustivel:
    requisitos_combustivel.append(converter_em_decimal(requisito))

def converter_em_snafu(numero):
    if numero == 0:
        return [0]
    
    casas = math.ceil(math.log(numero, 5)) + 1
    snafu = [0] * casas
    indice = 0
    while True:
        resto = valores_base[(numero % 5) + snafu[indice]]
        for i in range(0, len(resto)):
            snafu[indice + i] = resto[i]
        
        numero = numero // 5
        indice += 1

        if numero == 0:
            break
    
    snafu = snafu[::-1]
    if snafu[0] == 0:
        snafu.pop(0)
    
    return snafu

def imprimir_snafu(numero):
    snafu = ""
    for algarismo in numero:
        snafu += valor_decimal_caractere(algarismo)
    
    print(snafu)

# imprimir_snafu(converter_em_snafu(314159265))

soma_requisitos = sum(requisitos_combustivel)
imprimir_snafu(converter_em_snafu(soma_requisitos))