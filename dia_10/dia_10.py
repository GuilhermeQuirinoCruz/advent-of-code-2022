# arquivo_instrucoes = open("dia_10_exemplo.txt", "r")
arquivo_instrucoes = open("dia_10_input.txt", "r")
dados_instrucoes = arquivo_instrucoes.read()
lista_instrucoes = dados_instrucoes.split("\n")
arquivo_instrucoes.close()

# PARTE 1
valores_registrador = [1]
ciclo_atual = 0
somar_registrador = 0

for instrucao in lista_instrucoes:
    instrucao = instrucao.split(" ")

    valor_adicionar = valores_registrador[ciclo_atual] + somar_registrador
    valores_registrador.append(valor_adicionar)
    ciclo_atual += 1

    somar_registrador = 0

    if instrucao[0] == "addx":
       valores_registrador.append(valor_adicionar)
       ciclo_atual += 1
       somar_registrador = int(instrucao[1])

ciclos_interessantes = [20, 60, 100, 140, 180, 220]
soma_forcas_sinais = 0

for ciclo in ciclos_interessantes:
    soma_forcas_sinais += valores_registrador[ciclo] * ciclo

print("Soma da força dos sinais:")
print(soma_forcas_sinais)

# PARTE 2
def imprimir_monitor_crt():
    linha = ""
    for posicao in range(linhas_crt * colunas_crt):
        linha += monitor_crt[posicao]
        if (posicao + 1) % colunas_crt == 0:
            print(linha)
            linha = ""

linhas_crt = 6
colunas_crt = 40
monitor_crt = ""

for posicao in range(colunas_crt * linhas_crt):
    valor_atual_registrador = valores_registrador[posicao + 1]
    if abs(valor_atual_registrador - (posicao % colunas_crt)) < 2:
        monitor_crt += "#"
    else:
        monitor_crt += "."

print("Monitor CRT:")
imprimir_monitor_crt()