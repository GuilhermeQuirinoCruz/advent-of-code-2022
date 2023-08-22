import math

# arquivo_projeto = open("dia_19_exemplo.txt", "r")
# arquivo_projeto = open("dia_19_input.txt", "r")
# dados_projetos = arquivo_projeto.read()
# projetos = dados_projetos.split("\n")
# arquivo_projeto.close()

# projeto_teste = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."
projeto_teste = "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."

def tipo_recurso(recurso):
    match(recurso):
        case "ore":
            return 0
        case "clay":
            return 1
        case "obsidian":
            return 2
        case "geode":
            return 3

def custos_robos_projeto(projeto):
    custos = []
    projeto = projeto.split(":")[1]
    for dados_robo in projeto.split("."):
        dados_robo = dados_robo.split("robot costs")
        if dados_robo == [""]:
            continue

        custo_robo = []
        for recurso in dados_robo[1].strip(" ").split(" and "):
            recurso = recurso.split(" ")
            tipo = tipo_recurso(recurso[1])
            qtd = int(recurso[0])

            custo_robo.append(tuple([tipo, qtd]))
        
        custos.append(custo_robo)
    
    return custos

def recursos_suficientes_produzir(custo_robo, recursos):
    for recurso_necessario in custo_robo:
        tipo = recurso_necessario[0]
        qtd = recurso_necessario[1]
        if recursos[tipo] < qtd:
            return False
    
    return True

# pode substituir a função que analisa se há recursos suficientes para produzir um robô
# basta comparar o resultado com 0
def minutos_ate_robo(custo_robo, recursos, ganhos):
    minutos = 0
    for recurso_necessario in custo_robo:
        tipo = recurso_necessario[0]
        qtd = recurso_necessario[1]

        restante = qtd - recursos[tipo]
        if restante <= 0:
            continue
        
        if ganhos[tipo] == 0:
            return 100
        
        minutos = max(minutos, math.ceil(restante / ganhos[tipo]))
    
    return minutos

def produzir_robo(robo_produzir, custo_robo, recursos, ganhos):
    ganhos[robo_produzir] += 1
    for recurso_necessario in custo_robo:
        tipo = recurso_necessario[0]
        qtd = recurso_necessario[1]
        recursos[tipo] -= qtd
    
    return recursos, ganhos

def qualidade_projeto(projeto_analisar, indice_projeto):
    custos_robos = custos_robos_projeto(projeto_analisar)

    recursos_disponiveis = [0, 0, 0, 0]
    ganhos_por_minuto = [1, 0, 0, 0]

    duracao_simulacao = 24
    minuto_atual = 1
    while minuto_atual <= duracao_simulacao:
        minutos_ate_robos = []
        for i in range(4):
            minutos_ate_robos.append(minutos_ate_robo(custos_robos[i], recursos_disponiveis, ganhos_por_minuto))
        
        robo_produzir = -1
        maior_pontuacao = -1
        for robo in range(4):
            if not recursos_suficientes_produzir(custos_robos[robo], recursos_disponiveis):
                continue
            
            if robo == 3:
                robo_produzir = robo
                break

            novos_recursos, novos_ganhos = produzir_robo(
                robo, custos_robos[robo],
                recursos_disponiveis.copy(), ganhos_por_minuto.copy())
            pontuacao = 0

            for robo_seguinte in range(robo + 1, 4):
                novo_tempo = minutos_ate_robo(custos_robos[robo_seguinte], novos_recursos, novos_ganhos)
                pontuacao += (minutos_ate_robos[robo_seguinte] - novo_tempo) * robo_seguinte
            
            print(f"{robo}: {pontuacao}")
            if pontuacao >= maior_pontuacao:
                maior_pontuacao = pontuacao
                robo_produzir = robo

        for i in range(len(recursos_disponiveis)):
            recursos_disponiveis[i] += ganhos_por_minuto[i]
        
        if robo_produzir != -1:
            produzir_robo( robo_produzir, custos_robos[robo_produzir], recursos_disponiveis, ganhos_por_minuto)
        
        print(f"- Minuto {minuto_atual} -")
        print(ganhos_por_minuto)
        print(recursos_disponiveis)
        minuto_atual += 1
    
    return recursos_disponiveis[-1] * indice_projeto

qualidade_projeto(projeto_teste, 1)

# ao invés de olhar para o quanto um robô adianta a produção dos próximos, olhar para
# quantos deles é possível produzir no futuro