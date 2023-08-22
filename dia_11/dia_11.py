class Macaco:
    def __init__(self, itens, expressao, teste_divisibilidade, arremessar_verdadeiro, arremessar_falso):
        self.expressao = expressao
        self.teste_divisivel = teste_divisibilidade
        self.macaco_arremessar_verdadeiro = arremessar_verdadeiro
        self.macaco_arremessar_falso = arremessar_falso

        self.itens = []
        for item in itens:
            self.receber_item(item)

        self.itens_inspecionados = 0
    
    def receber_item(self, item):
        # if item % self.teste_divisivel != 0:
        #     item = item % self.teste_divisivel
        
        self.itens.append(item)

def operacao_inspecao(expressao, item):
    expressao = expressao.split(" ")
    v1 = item if expressao[0] == "old" else int(expressao[0])
    operacao = expressao[1]
    v2 = item if expressao[2] == "old" else int(expressao[2])
    
    if operacao == "+":
        return v1 + v2
    
    return v1 * v2

# arquivo_macacos = open("dia_11_exemplo.txt", "r")
arquivo_macacos = open("dia_11_input.txt", "r")
dados_macacos = arquivo_macacos.read()
info_macacos = dados_macacos.split("\n")
arquivo_macacos.close()

macacos = []
multiplicacao_mod = 1

for i in range(0, len(info_macacos), 7):
    itens_macaco = []
    for item in info_macacos[i + 1].split(":")[1].split(","):
        itens_macaco.append(int(item.strip(" ")))

    expressao = info_macacos[i + 2].split(":")[1].split("=")[1].strip(" ")
    
    teste_divisibilidade = int(info_macacos[i + 3].split(" ")[-1])
    
    arremessar_verdadeiro = int(info_macacos[i + 4].split(" ")[-1])
    arremessar_falso = int(info_macacos[i + 5].split(" ")[-1])

    novo_macaco = Macaco(itens_macaco, expressao, teste_divisibilidade, arremessar_verdadeiro, arremessar_falso)
    macacos.append(novo_macaco)

    multiplicacao_mod *= teste_divisibilidade

def simular_round(divisao_preocupacao):
    for macaco in macacos:
        macaco.itens.reverse()

        while len(macaco.itens) > 0:
            macaco.itens_inspecionados += 1

            item = macaco.itens.pop() % multiplicacao_mod
            item = operacao_inspecao(macaco.expressao, item) // divisao_preocupacao

            macaco_receber = -1
            if item % macaco.teste_divisivel == 0:
                macaco_receber = macaco.macaco_arremessar_verdadeiro
            else:
                macaco_receber = macaco.macaco_arremessar_falso
            
            macacos[macaco_receber].receber_item(item)

def imprimir_macacos():
    for macaco in macacos:
        print(f"Itens:{macaco.itens}")
        print(f"Quantidade de itens inspecionados: {macaco.itens_inspecionados}")

# PARTE 1
# qtd_rounds = 20
# for round in range(qtd_rounds):
#     simular_round(3)

# PARTE 2
qtd_rounds = 10000
for round in range(qtd_rounds):
    simular_round(1)

imprimir_macacos()
macacos.sort(key = lambda m:m.itens_inspecionados, reverse=True)
print(f"Os macacos mais ativos inspecionaram {macacos[0].itens_inspecionados} e {macacos[1].itens_inspecionados} itens")
print(f"Os dois valores multiplicados: {macacos[0].itens_inspecionados * macacos[1].itens_inspecionados}")