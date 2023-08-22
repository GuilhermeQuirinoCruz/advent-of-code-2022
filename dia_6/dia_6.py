# arquivo_buffer = open("dia_6_exemplo.txt", "r")
arquivo_buffer = open("dia_6_input.txt", "r")
dados_buffer = arquivo_buffer.read()
arquivo_buffer.close()

# exemplos
# dados_buffer = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# dados_buffer = "nppdvjthqldpwncqszvftbrmjlhg"
# dados_buffer = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# dados_buffer = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def caracteres_repetidos(sequencia):
    for caracter in sequencia:
        if sequencia.count(caracter) > 1:
            return True
    
    return False

def indice_sequencia_caracteres_distintos(tamanho_sequencia):
    inicio_sequencia = 0
    fim_sequencia = tamanho_sequencia

    while caracteres_repetidos(dados_buffer[inicio_sequencia:fim_sequencia]):
        inicio_sequencia += 1
        fim_sequencia += 1

    return fim_sequencia

# PARTE 1
print(indice_sequencia_caracteres_distintos(4))

# PARTE 2
print(indice_sequencia_caracteres_distintos(14))