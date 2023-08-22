from sympy import sympify, solve

# arquivo_macacos = open("dia_21_exemplo.txt", "r")
arquivo_macacos = open("dia_21_input.txt", "r")
dados_macacos = arquivo_macacos.read()
arquivo_macacos.close()

macacos = {}
for macaco in dados_macacos.split("\n"):
    macaco = macaco.split(":")
    macacos[macaco[0]] = macaco[1].strip(" ")

def numero_macaco(macaco):
    expressao = macacos[macaco]
    if expressao.isnumeric():
        return expressao
    
    termos = expressao.split(" ")
    expressao = expressao.replace(termos[0], numero_macaco(termos[0]))
    expressao = expressao.replace(termos[2], numero_macaco(termos[2]))

    return str(int(eval(expressao)))

# PARTE 1
# print(numero_macaco("root"))

# PARTE 2
def expressao_root(macaco):
    if macaco == "humn":
        return "humn"
    
    expressao = macacos[macaco]
    if expressao.isnumeric():
        return expressao
    
    termos = expressao.split(" ")
    expressao = expressao.replace(termos[0], expressao_root(termos[0]))
    expressao = expressao.replace(termos[2], expressao_root(termos[2]))

    return f"({expressao})" if "humn" in expressao else str(int(eval(expressao)))

macacos["root"] = macacos["root"].replace("+", ",")

expressao = expressao_root("root")

equacao = sympify("Eq" + expressao)
solucao = solve(equacao)
print(solucao)