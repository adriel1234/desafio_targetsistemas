def sequencia_aritmetica(sequence):
    return sequence[-1] + (sequence[1] - sequence[0])

def sequencia_geometrica(sequence):
    ratio = sequence[1] / sequence[0]
    return sequence[-1] * ratio

def sequencia_quadrado(sequence):
    n = int(sequence[-1]**0.5) + 1
    return n**2

def next_even_square_term(sequence):
    n = int(sequence[-1]**0.5) + 2
    return n**2

def next_fibonacci_term(sequence):
    return sequence[-1] + sequence[-2]

def next_custom_sequence_term(sequence):
    last_increment = sequence[-1] - sequence[-2]
    return sequence[-1] + last_increment

# Sequências
sequence_a = [1, 3, 5, 7]
sequence_b = [2, 4, 8, 16, 32, 64]
sequence_c = [0, 1, 4, 9, 16, 25, 36]
sequence_d = [4, 16, 36, 64]
sequence_e = [1, 1, 2, 3, 5, 8]
sequence_f = [2, 10, 12, 16, 17, 18, 19]


next_term_a = sequencia_aritmetica(sequence_a)
next_term_b = int(sequencia_geometrica(sequence_b))  
next_term_c = sequencia_quadrado(sequence_c)
next_term_d = next_even_square_term(sequence_d)
next_term_e = next_fibonacci_term(sequence_e)
next_term_f = next_custom_sequence_term(sequence_f)

# Impressão dos resultados
print(f"Próximo termo da sequência a) é: {next_term_a}")
print(f"Próximo termo da sequência b) é: {next_term_b}")
print(f"Próximo termo da sequência c) é: {next_term_c}")
print(f"Próximo termo da sequência d) é: {next_term_d}")
print(f"Próximo termo da sequência e) é: {next_term_e}")
print(f"Próximo termo da sequência f) é: {next_term_f}")
