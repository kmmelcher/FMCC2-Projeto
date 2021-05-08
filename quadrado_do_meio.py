import time

def tempo_aleatorio():
    """ Retorna um número aleatório de 4 dígitos
    Esse número são os últimos 4 digitos do tempo, em nanossegundos, desde que
    seu computador ligou """
    return int(str(time.clock_gettime_ns(time.CLOCK_BOOTTIME))[4:])

def quadrado_do_meio(semente=tempo_aleatorio()):
    """ Retorna o período de repetição de uma semente do algoritmo do quadrado
    do meio.
    Se nenhuma semente for passada, será uma semente aleatória. """
    numero = semente
    periodo = set()

    while numero not in periodo:
        periodo.add(numero)
        numero = int(str(numero * numero).zfill(8)[2:6])

    return periodo

def numero_aleatorio(digitos):
    """ Retorna uma número aleatório com a quantidade de dígitos de 0 até a
    passada como parâmetro, usando o algoritmo do quadrado do meio. """
    zeros = digitos * 2
    comeco = (zeros//2) - (digitos//2)
    fim =  (zeros//2) + (digitos//2)

    return int(str( tempo_aleatorio() ** 2 ).zfill(zeros)[comeco:fim])

print ("O período de números aleatórios é " + str(quadrado_do_meio()))
print ("Número aleatório: " + str(numero_aleatorio(7)))
