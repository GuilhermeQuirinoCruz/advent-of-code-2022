# arquivo_secoes = open("dia_4_exemplo.txt", "r")
arquivo_secoes = open("dia_4_input.txt", "r")
dados_secoes = arquivo_secoes.read()
lista_secoes = dados_secoes.split("\n")
arquivo_secoes.close()

def intervalo_contido(intervalo1, intervalo2):
    return intervalo1[0] <= intervalo2[0] and intervalo1[1] >= intervalo2[1]

contidos = 0

# PARTE 1
for par_secoes in lista_secoes:
    pares = par_secoes.split(",")

    par1 = list(map(int, pares[0].split("-")))
    par2 = list(map(int, pares[1].split("-")))

    if intervalo_contido(par1, par2) or intervalo_contido(par2, par1):
        contidos += 1

print(contidos)

# PARTE 2
def intervalo_sobrepoe(intervalo1, intervalo2):
    return (intervalo1[0] >= intervalo2[0] and intervalo1[0] <= intervalo2[1]) \
        or (intervalo1[1] >= intervalo2[0] and intervalo1[1] <= intervalo2[1])

sobreposicoes = 0

for par_secoes in lista_secoes:
    pares = par_secoes.split(",")

    par1 = list(map(int, pares[0].split("-")))
    par2 = list(map(int, pares[1].split("-")))

    if intervalo_sobrepoe(par1, par2) or intervalo_sobrepoe(par2, par1):
        sobreposicoes += 1

print(sobreposicoes)