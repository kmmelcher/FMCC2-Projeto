import time

def gera_semente_aleatoria():
    """ Retorna uma semente aleatória de 4 dígitos
    Essa semente é composta pelos últimos 4 digitos do tempo, em nanossegundos,
    desde que o computador atual ligou """
    return int(str(time.clock_gettime_ns(time.CLOCK_BOOTTIME))[4:])

def quadrado_do_meio(semente):
    """ Retorna o período de repetição de uma semente do algoritmo do quadrado
    do meio.
    Se nenhuma semente for passada, será uma semente aleatória. """
    if not semente:
        semente = gera_semente_aleatoria()
    
    numero = int(semente)
    periodo = set()

    while numero not in periodo:
        periodo.add(numero)
        numero = int(str(numero * numero).zfill(8)[2:6])

    return periodo

def menu():
    mensagem = "\n\nQual algoritmo você deseja usar?"
    mensagem += "\n(1) - Algoritmo do quadrado do meio"
    mensagem += "\n(2) - Algoritmo da congruência linear"
    mensagem += "\n(3) - Sair\n\n"

    while True:
        escolha = int(input(mensagem))
        if escolha == 1:
            semente = input("Insira uma semente: ")
            periodo = quadrado_do_meio(semente)
            print (f"Essa semente gerou uma sequência de números aleatórios que se repetem a cada {len(periodo)} elementos")
            print ("Conjunto dos elementos gerados: \n" + str(periodo))
        elif escolha == 2:
            pass
        elif escolha == 3:
            break
    
menu()

