class Arquivo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

class Diretorio:
    def __init__(self, nome, diretorio_pai):
        self.nome = nome
        self.diretorio_pai = diretorio_pai
        self.tamanho = 0
        self.subdiretorios = []
        self.arquivos = []

    def acessar_subdiretorio(self, nome):
        for diretorio in self.subdiretorios:
            if diretorio.nome == nome:
                return diretorio
        
        return self

    def atualizar_tamanho_subdiretorios(self):
        tamanho_subdiretorios = 0
        for subdiretorio in self.subdiretorios:
            tamanho_subdiretorios += subdiretorio.atualizar_tamanho_subdiretorios()
        
        self.tamanho += tamanho_subdiretorios
        return self.tamanho


# arquivo_terminal = open("dia_7_exemplo.txt", "r")
arquivo_terminal = open("dia_7_input.txt", "r")
dados_terminal = arquivo_terminal.read()
lista_comandos = dados_terminal.split("\n")
arquivo_terminal.close()

lista_diretorios = []

diretorio_raiz = Diretorio("/", None)
lista_diretorios.append(diretorio_raiz)
diretorio_atual = diretorio_raiz

def interpretar_comando(comando):
    global diretorio_atual
    if comando[1] == "cd":
        if comando[2] == "..":
            diretorio_atual = diretorio_atual.diretorio_pai
        else:
            diretorio_atual = diretorio_atual.acessar_subdiretorio(comando[2])

def interpretar_linha(linha):
    match(linha[0]):
        case "$":
            interpretar_comando(linha)
        case "dir":
            novo_diretorio = Diretorio(linha[1], diretorio_atual)
            diretorio_atual.subdiretorios.append(novo_diretorio)

            lista_diretorios.append(novo_diretorio)

            print(f"Diretório criado: {novo_diretorio.nome}")
        case _:
            tamanho_arquivo = int(linha[0])
            novo_arquivo = Arquivo(linha[1], tamanho_arquivo)
            diretorio_atual.arquivos.append(novo_arquivo)
            diretorio_atual.tamanho += tamanho_arquivo

            print(f"Arquivo criado: {novo_arquivo.nome}")

for linha in lista_comandos[1:]:
    linha = linha.split(" ")
    interpretar_linha(linha)

diretorio_raiz.atualizar_tamanho_subdiretorios()

def somar_tamanhos_menores_100k():
    soma = 0

    for diretorio in lista_diretorios:
        if diretorio.tamanho <= 100000:
            soma += diretorio.tamanho

    return soma

for diretorio in lista_diretorios:
    print(f"{diretorio.nome}, {diretorio.tamanho}K")

# PARTE 1
print("Soma dos tamanhos menores que 100k:")
print(somar_tamanhos_menores_100k())

# PARTE 2
espaco_total_disco = 70000000
espaco_necessario_atualizacao = 30000000

espaco_disponivel_disco = espaco_total_disco - diretorio_raiz.tamanho
tamanho_minimo_deletar = espaco_necessario_atualizacao - espaco_disponivel_disco
print("Tamanho necessário para a atualização:")
print(tamanho_minimo_deletar)

menor_tamanho_deletar = diretorio_raiz.tamanho

for diretorio in lista_diretorios:
    if diretorio.tamanho >= tamanho_minimo_deletar and diretorio.tamanho < menor_tamanho_deletar:
        menor_tamanho_deletar = diretorio.tamanho

print("Menor tamanho de diretório possível para alocar espaço para a atualização:")
print(menor_tamanho_deletar)