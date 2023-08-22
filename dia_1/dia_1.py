# PARTE 1
# abre o arquivo de texto com os dados em modo de leitura
arquivo_elfos = open("dia_1_input.txt", "r")

# lê os arquivos na variável 'dados'
dados = arquivo_elfos.read()

# separa a string em uma lista, separando os dados pelo '\n'
lista_calorias = dados.split('\n')

# fecha o arquivo
arquivo_elfos.close()

# guarda as somas em uma lista
calorias_elfos = []

# guarda as maiores somas
maiores_somas_calorias = []

# conta o total que cada elfo carrega
total_calorias = 0

# passa por cada item da lista, soma o valor caso seja diferente de vazio
for cal in lista_calorias:
    # soma as calorias no total
    if cal != '':
        total_calorias += int(cal)
    else:
        # adiciona o total na lista
        calorias_elfos.append(total_calorias)

        # redefine o total
        total_calorias = 0

# imprime a maior soma encontrada
print(max(calorias_elfos))

# PARTE 2
# adiciona as maiores somas em uma lista e remove da lista original
for i in range(0, 3):
    maiores_somas_calorias.append(max(calorias_elfos))
    calorias_elfos.remove(maiores_somas_calorias[i])

# imprime a soma das maiores somas
print(sum(maiores_somas_calorias))